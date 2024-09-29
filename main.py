from flask import Flask, request, Response
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.messages import ContactMessage


from viberbot.api.viber_requests import ViberMessageRequest, ViberConversationStartedRequest
from keyboards import share_phone_keyboard
from messages import main_menu_message, contact_recived_message, send_rich_media_with_links, conversation_started_message, \
    send_contact_keyboard, send_contacts, send_location, settings_message, send_change_phone_number, send_my_order_message, \
    send_order_history
from queries import get_number_from_user_id

from settings import settings

app = Flask(__name__)
viber = Api(BotConfiguration(
    name='Cosmy',
    avatar=' ',
    auth_token=settings.auth_token
))



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
                    case _ if "https://" in message.text:
                        pass
                    case str():
                        main_menu_message(message, viber_request, viber)
                      
            
                
            else:
                viber.send_messages(viber_request.sender.id, [
                    TextMessage(text="Для авторизації,\nпідтвердіть свій номер телефону.\n Потрібно лише натиснути на кнопку ", 
                                    keyboard=share_phone_keyboard, 
                                    min_api_version=3)
            ])


    # First message from bot
    if isinstance(viber_request, ViberConversationStartedRequest):
        conversation_started_message(viber, viber_request)

    
    return Response(status=200)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, 
    )