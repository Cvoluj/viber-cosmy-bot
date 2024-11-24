from viberbot.api.messages.text_message import TextMessage
from viberbot.api.messages import PictureMessage, KeyboardMessage, RichMediaMessage, LocationMessage
from viberbot.api.messages.data_types.location import Location


from keyboards import WHITE_BORDER, format_text_with_color, main_keyboard, rich_media_links_part2, rich_media_links_part1, contacts_keyboard, map_keyboard, menu_keyboard, \
    settings_keyboard, share_phone_keyboard, no_orders_keyboard, buttons_settings, menu_button
from queries import add_user_to_db
from settings import settings
from queries import get_number_from_user_id
from api import get_all_last_orders_by_telephone, get_last_order_by_telephone
from utils import format_order_data

expose_url = settings.expose_url


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
    # if order and order.get('order_status') in ["В очікуванні", "В дорозі"]:
    order_details = format_order_data(order_data)
    send_order_data_to_user(viber_request, viber, order_details)
    # else:
        # send_no_orders(viber_request, viber)


def send_order_data_to_user(viber_request, viber, order_details):
    if not order_details:
        return
    
    response_message = "\n".join([f"{key}: {value}" for key, value in order_details.items() if key != "Товари у замовленні"])
    products_message = "Товари у замовленні:\n" + "\n".join(order_details["Товари у замовленні"])
    full_message = f"{response_message}\n\n{products_message}"

    viber.send_messages(
    viber_request.sender.id,
    [
        TextMessage(text=full_message,
                    keyboard=main_keyboard,
                    min_api_version=6
                    )
    ]
    )

def send_no_orders(viber_request, viber):
    viber.send_messages(
        viber_request.sender.id,
        [
            TextMessage(text='*У вас ще не було замовлень, але це легко виправити 😉*',
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
    
    
def show_order(viber_request, viber, orders_data, index):
    orders = orders_data.get("orders")
    orders_keys = [*orders.keys()]
    order = orders.get(orders_keys[index])

    order_details = format_order_data({'order': order})

    response_message = "\n".join([f"{key}: {value}" for key, value in order_details.items() if key != "Товари у замовленні"])
    products_message = "Товари у замовленні:\n" + "\n".join(order_details["Товари у замовленні"])
    full_message = f"{response_message}\n\n{products_message}"

    # Navigation buttons
    # if index > 0:
    #     nav_keyboard.add(types.InlineKeyboardButton("<", callback_data=f"prev_order_{index}"))
    # nav_keuyboard.add(types.InlineKeyboardButton("Меню", callback_data="main_menu"))
    # if index < len(orders_data) - 1:
    #     nav_keyboard.add(types.InlineKeyboardButton(">", callback_data=f"next_order_{index}"))

    next_page = {
        "Columns": 2,
        "Rows": 1,
        "Text": format_text_with_color('❯'),
        "ActionBody": f"> {index + 1}",
        **buttons_settings   
    }
        
    prev_page = {
        "Columns": 2,
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
