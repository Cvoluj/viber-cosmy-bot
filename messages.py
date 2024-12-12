import threading
import time
from flask import Response
import requests
from copy import deepcopy
from dataclasses import dataclass
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.messages import PictureMessage, KeyboardMessage, RichMediaMessage, LocationMessage, VideoMessage
from viberbot.api.messages.data_types.location import Location


from keyboards import MILKY_COLOR, WHITE_BORDER, format_text_with_color, main_keyboard, rich_media_links_part2, rich_media_links_part1, contacts_keyboard, map_keyboard, menu_keyboard, \
    settings_keyboard, share_phone_keyboard, no_orders_keyboard, buttons_settings, menu_button, admin_keyboard, base_rich_media, frame
from queries import add_user_to_db, get_is_admin_from_user_id, get_user_ids, give_admin_rules
from settings import settings
from queries import get_number_from_user_id
from api import get_all_last_orders_by_telephone, get_last_order_by_telephone
from utils import format_order_data, split_on_batches, validate_url
from waiters_list import waiters, Waiter

expose_url = settings.expose_url
VIBER_BROADCAST_URL = "https://chatapi.viber.com/pa/broadcast_message"


def conversation_started_message(viber, viber_request):
    user_id = viber_request.user.id
    viber.send_messages(
        user_id,
        [
            TextMessage(text="Привіт! Це бот Cosmy. Надішліть будь-яке повідомлення, щоб почати роботу")
        ]
    )

def main_menu_message(message, viber_request, viber):
    print(viber_request)
    print(message)
    viber.send_messages(viber_request.sender.id, [
        PictureMessage(
            media=f'{expose_url}/static/cosmy.jpg', 
            min_api_version=6),
    ])
    viber.send_messages(viber_request.sender.id, [
            TextMessage(
            text="Вітаю🌷 На зв’язку Cosmy асистент 👱🏻‍♀️\nЧим можу бути тобі корисною?"),
            KeyboardMessage(keyboard=main_keyboard, min_api_version=6)
    ])
    # viber.send_messages(viber_request.sender.id, [
    #     KeyboardMessage(keyboard=main_keyboard, min_api_version=3)
    # ])


def contact_recived_message(message, viber_request, viber):
    phone_number = message.contact.phone_number
    
    if phone_number:
        add_user_to_db(
            viber_request.sender.id,
            phone_number,
            is_admin=0, 
        )
        main_menu_message(message, viber_request, viber)

def send_rich_media_with_links(viber_request, viber):
    viber.send_messages(viber_request.sender.id, [
        TextMessage(text="❓ Інформація. Що вас цікавить?", min_api_version=6),
        RichMediaMessage(rich_media=rich_media_links_part1, min_api_version=6),
        RichMediaMessage(rich_media=rich_media_links_part2, min_api_version=6)
    ])

def send_contact_keyboard(viber_request, viber):
    viber.send_messages(viber_request.sender.id, [
        TextMessage(
            text="Оберіть, що вас цікавить 👇🏻",
            keyboard=contacts_keyboard, 
            min_api_version=6
            ),
    ])

def send_contacts(viber_request, viber):
    viber.send_messages(viber_request.sender.id, [
        TextMessage(text="Наші контакти:\n\n🌃 м. Київ\nЛабораторний провулок 7, офіс 14\n\nТелефон:\n📞066 288 48 11\n📞073 317 54 43\n📞067 820 58 48\n\n" +
                    "📮 Електронна пошта: cosmy.com.ua@gmail.com\n\n" + 
                    "⌚️Час роботи:\nПн-Пт 9:00-18:00\nСб 10:00-18:00\nНд - Вихідний"
        ,keyboard=map_keyboard,
        min_api_version=6           
                
        ),
    ])

def send_location(viber_request, viber):
    location = Location(lat=50.42801141925601,
                        lon=30.52523747997809)
    # https://www.google.com/maps?q=50.42801141925601,30.52523747997809
    viber.send_messages(
        viber_request.sender.id, [
            LocationMessage(location=location, keyboard=menu_keyboard, min_api_version=6)
        ]

    )

def settings_message(viber_request, viber):
    viber.send_messages(
        viber_request.sender.id, [
            PictureMessage(
                media=f'{expose_url}/static/cosmy.jpg',
            )]
    )
    viber.send_messages(
        viber_request.sender.id, [
            TextMessage(
                text="🔄 Бажаєте змінити номер телефону?"),
            KeyboardMessage(
                keyboard=settings_keyboard,
                min_api_version=6
            )
        ]
    )

def send_change_phone_number(viber_request, viber):
    viber.send_messages(
        viber_request.sender.id,
        [        
            TextMessage(
                text="*Будь ласка, поділіться своїм номером телефону для авторизації.*",
                keyboard=share_phone_keyboard, 
                min_api_version=6),
        ]
    )

def send_my_order_message(viber_request, viber):
    if not settings.cosmy_api_token:
        viber.send_messages(viber_request.sender.id,
            [
                TextMessage(text="Помилка при логіні. Спробуйте ще раз")
            ]
        )
        return

    number = get_number_from_user_id(viber_request.sender.id)
    if not number:
        viber.send_messages(viber_request.sender.id,
            [
                TextMessage(text="Не знайдено номер телефону. Переконайтеся, що ви зареєстровані.")
            ]
        )
        return

    order_data = get_last_order_by_telephone(number)
    print(order_data)
    if order_data is None or 'order' not in order_data.keys():
        send_no_orders(viber_request, viber)
        return
    
    order = order_data.get('order')
    if order and order.get('order_status') in ["В очікуванні", "В дорозі"]:
        order_details = format_order_data(order_data)
        send_order_data_to_user(viber_request, viber, order_details)
    else:
        send_no_orders(viber_request, viber, text="*Ви наразі не очікуєте доставку або не робили замовлення, все в ваших руках*")


def send_order_data_to_user(viber_request, viber, order_details):
    if not order_details:
        return
    
    response_message = "\n".join([f"{key}: {value}" for key, value in order_details.items() if key not in ("Товари у замовленні", "Посилання")])
    products_message = "Товари у замовленні:\n" + "\n".join(order_details["Товари у замовленні"])
    url_message = "Посилання на товар:\n" + "\n".join(order_details["Посилання"])
    full_message = f"{response_message}\n\n{products_message}\n{url_message}"

    viber.send_messages(
    viber_request.sender.id,
    [
        TextMessage(text=full_message,
                    keyboard=main_keyboard,
                    min_api_version=6
                    )
    ]
    )

def send_no_orders(viber_request, viber, text="*У вас ще не було замовлень, але це легко виправити 😉*"):
    viber.send_messages(
        viber_request.sender.id,
        [
            TextMessage(text=text,
                        keyboard=no_orders_keyboard, min_api_version=6)
        ]
    )

def send_order_history(viber_request, viber, index=0):
    if not settings.cosmy_api_token:
        viber.send_messages(
            viber_request.sender.id,
            [
                TextMessage(text="Помилка при логіні. Спробуйте ще раз")
            ]
        )
        return

    number = get_number_from_user_id(viber_request.sender.id)
    if not number:
        viber.send_messages(viber_request.sender.id,
            [
                TextMessage(text="Не знайдено номер телефону. Переконайтеся, що ви зареєстровані.")
            ]
        )
        return

    orders_data = get_all_last_orders_by_telephone(number)

    if not orders_data or len(orders_data) == 0:
        send_no_orders(viber_request, viber)
        return
    
    show_order(viber_request, viber, orders_data, index)
    return
    
    
def show_order(viber_request, viber, orders_data, index):
    orders = orders_data.get("orders")
    orders_keys = [*orders.keys()]
    order = orders.get(orders_keys[index])

    order_details = format_order_data({'order': order})

    response_message = "\n".join([f"{key}: {value}" for key, value in order_details.items() if key not in ("Товари у замовленні", "Посилання")])
    products_message = "Товари у замовленні:\n" + "\n".join(order_details["Товари у замовленні"])
    url_message = "Посилання на товар:\n" + "\n".join(order_details["Посилання"])
    full_message = f"{response_message}\n\n{products_message}\n{url_message}"

    next_page = {
        "Columns": 3,
        "Rows": 1,
        "Text": format_text_with_color('❯'),
        "ActionBody": f"> {index + 1}",
        **buttons_settings   
    }
        
    prev_page = {
        "Columns": 3,
        "Rows": 1,
        "Text": format_text_with_color('❮'),
        "ActionBody": f"< {index - 1}",
        **buttons_settings,
    }


    keyboard_indexing = {
        "Type": "keyboard",
        "ButtonsGroupColumns": 6,  
        "ButtonsGroupRows": 6,
        "BgColor": WHITE_BORDER,
        "Buttons": [
            prev_page,
            next_page,
            menu_button
        ]
    }



    viber.send_messages(viber_request.sender.id,
            [   
                TextMessage(text=full_message, keyboard=keyboard_indexing, min_api_version=6),
            ]
        )
    return

def greet_new_admin(viber_request, viber):
    is_admin = give_admin_rules(viber_request.sender.id)

    if is_admin[0] == 1:
        viber.send_messages(viber_request.sender.id,
            [
                TextMessage(text="Вітаємо, у вас тепер права адміністратора, ви можете надсилати відео!")
            ]
        )

    return

def send_admin_keyboard(viber_request, viber):
    is_admin = get_is_admin_from_user_id(viber_request.sender.id)

    if is_admin != 1:
        main_menu_message("Not admin", viber_request, viber)
        return
    
    viber.send_messages(
        viber_request.sender.id,
        [
            TextMessage(text="Адмін панель", keyboard=..., min_api_version=6)
        ]
    )


@dataclass
class Broadcast:
    func: PictureMessage | VideoMessage
    kwargs: dict[str | None]
    thumbnail: str | None
    media: str | None
    type: str
    url_button: str | None = None


def prepare_broadcast_message(viber_request, viber, media_url, thumbnail):
    if '/image/' in media_url:
        func = PictureMessage
        kwargs = {}
        type = "picture"
    if '/video/' in media_url:
        func = VideoMessage
        kwargs = {"size":1, "duration": 180}
        type = "video"

    viber.send_messages(
        viber_request.sender.id,
        [
            func(text=thumbnail, min_api_version=6, media=media_url, **kwargs, keyboard=admin_keyboard)
        ]
    )
    return Broadcast(func=func, kwargs=kwargs, thumbnail=thumbnail, media=media_url, type=type)

def add_url_button(viber_request, viber, is_retry=False):
    if not is_retry:
        viber.send_messages(
            viber_request.sender.id,
            [
                TextMessage(text="Надішліть посилання", min_api_version=6)
            ]
        )
    else:
        viber.send_messages(
            viber_request.sender.id,
            [
                TextMessage(text="Надішліть валідне посилання", min_api_version=6)
            ]
        )

    waiters[viber_request.sender.id] = Waiter(
        recieved_message=None, 
        sender_id=viber_request.sender.id,
        is_waiting=True
    )
    return

def handle_url_message(viber_request, viber, waiter: Waiter, message_text):
    validated_message = validate_url(message_text)
    if not validated_message:
        add_url_button(viber_request, viber, is_retry=True)
        return Response(status=200)

    waiter.recieved_message = validated_message
    waiter.is_waiting = False

    viber.send_messages(
        viber_request.sender.id,
        [
            TextMessage(text=f"Посилання додано до розсилки!\n{waiter.recieved_message}", min_api_version=6, keyboard=admin_keyboard)
        ]
    )
    return 


def send_broadcast(viber_request, viber, broadcast: Broadcast):
    headers = {
        "X-Viber-Auth-Token": settings.auth_token,
        "Content-Type": "application/json"
    }
    user_ids = get_user_ids()
    user_ids_batches = split_on_batches(user_ids, 150)
    batch_thread = threading.Thread(target=send_broadcast_message, args=(viber_request, viber, user_ids_batches, headers, broadcast))
    batch_thread.start()

def send_broadcast_message(viber_request, viber, batch, headers, broadcast: Broadcast):
    waiter = waiters.get(viber_request.sender.id)
    rich_button_url = ""
    if waiter.recieved_message:
        rich_button_url = {
            "Columns": 6,
            "Rows": 1,
            "ActionType": "open-url",
            "ActionBody": waiter.recieved_message,
            "Text": format_text_with_color("Детальніше..."),
            "TextSize": "large",
            "TextVAlign": "middle",
            "TextHAlign": "center",
            "BgColor": MILKY_COLOR,
            "Silent": True,
            "OpenURLType": "internal",
            "Frame": frame
        }

        waiter.recieved_message = ""

    for users in batch:
        deepcopy_base_rich_media = deepcopy(base_rich_media)

        if rich_button_url != "":
            deepcopy_base_rich_media["Buttons"].insert(0, rich_button_url)
            deepcopy_base_rich_media["ButtonsGroupRows"] = 2

        payload = {
            "broadcast_list": users,
            "text": broadcast.thumbnail,
            "media": broadcast.media,
            "type":broadcast.type,
            **broadcast.kwargs,
        }

        rich_media_payload = {
            "broadcast_list": users,
            "min_api_version":6,
            "type":"rich_media",
            "rich_media": deepcopy_base_rich_media
        }
        try:
            response_base = requests.post(VIBER_BROADCAST_URL, json=payload, headers=headers)
            response_rich_media = requests.post(VIBER_BROADCAST_URL, json=rich_media_payload, headers=headers)
            print(f"Sent batch: {users}, Response: {response_base.status_code}, {response_base.text}")
        except requests.RequestException as e:
            print(f"Error sending batch: {users}, Error: {e}")
        time.sleep(11)