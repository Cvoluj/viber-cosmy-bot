from flask import Flask, request, Response
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.messages import ContactMessage, VideoMessage, PictureMessage


from viberbot.api.viber_requests import ViberMessageRequest, ViberConversationStartedRequest
from api.startup_login import startup_login
from keyboards import share_phone_keyboard
from messages import add_url_button, greet_new_admin, main_menu_message, contact_recived_message, prepare_broadcast_message, send_broadcast, send_rich_media_with_links, conversation_started_message, \
    send_contact_keyboard, send_contacts, send_location, settings_message, send_change_phone_number, send_my_order_message, send_order_history
from queries import get_is_admin_from_user_id, get_number_from_user_id

from settings import settings

app = Flask(__name__)
viber = Api(BotConfiguration(
    name='Cosmy',
    avatar=' ',
    auth_token=settings.auth_token
))
startup_login()
global broadcast
broadcast = None

@app.route('/', methods=['POST'])
def incoming():
    
    
    if not viber.verify_signature(request.get_data(), request.headers.get('X-Viber-Content-Signature')):
        return Response(status=403)

    viber_request = viber.parse_request(request.get_data())
    if isinstance(viber_request, ViberMessageRequest):
        message = viber_request.message
        
        if isinstance(message, ContactMessage):
            contact_recived_message(message, viber_request, viber)

        if isinstance(message, TextMessage):
            print(message)
            if get_number_from_user_id(viber_request.sender.id):
                admin_pattern = f"admin {settings.admin_password}"
                match message.text:
                    case "Information":
                        send_rich_media_with_links(viber_request, viber)
                    case "Menu":
                        main_menu_message(message, viber_request, viber)
                    case "ContactCenter":
                        send_contact_keyboard(viber_request, viber)
                    case "Contacts":
                        send_contacts(viber_request, viber)
                    case "Map":
                        send_location(viber_request, viber)
                    case "Settings":
                        settings_message(viber_request, viber)
                    case "ChangePhoneNumber":
                        send_change_phone_number(viber_request, viber)
                    case "MyOrder":
                        send_my_order_message(viber_request, viber)
                    case "OrderHistory":
                        send_order_history(viber_request, viber)
                    case "Broadcast":
                        is_admin = get_is_admin_from_user_id(viber_request.sender.id)
                        if is_admin != 1:
                            return
                        
                        send_broadcast(viber_request, viber, broadcast)
                    case "Add Url":
                        is_admin = get_is_admin_from_user_id(viber_request.sender.id)
                        if is_admin != 1:
                            return
                        
                        add_url_button(viber_request, viber, broadcast)
                    case _:
                        if message.text == admin_pattern:
                            greet_new_admin(viber_request, viber)
                        elif message.text.startswith("<") or message.text.startswith(">"):
                            send_order_history(viber_request, viber, index=int(message.text.split(" ")[-1]))
                        elif "https://"  in message.text or "viber://chat?number=" in message.text:
                            print("do not react")
                        else:
                            main_menu_message(message, viber_request, viber)

            
                
            else:
                viber.send_messages(viber_request.sender.id, [
                    TextMessage(text="Для авторизації,\nпідтвердіть свій номер телефону.\n Потрібно лише натиснути на кнопку ", 
                                    keyboard=share_phone_keyboard, 
                                    min_api_version=6)
            ])
        
        if isinstance(message, VideoMessage) or isinstance(message, PictureMessage):
            is_admin = get_is_admin_from_user_id(viber_request.sender.id)

            if is_admin != 1:
                return Response(status=200)

            broadcast = prepare_broadcast_message(viber_request, viber, message.media, message.text) 

    # First message from bot
    if isinstance(viber_request, ViberConversationStartedRequest):
        conversation_started_message(viber, viber_request)

    
    return Response(status=200)

def run_app():
    app.run(host='0.0.0.0', port=5000, debug=True, 
    )

if __name__ == "__main__":
    run_app()