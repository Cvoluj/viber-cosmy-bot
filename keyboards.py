BORDO_COLOR = "#7e2129"
MILKY_COLOR = "#f4e9ea"
WHITE_BORDER = "#ffffff"

CONTACT_KEYBOARD_BG_COLOR = "#7e2129"


def format_text_with_color(text, text_color=BORDO_COLOR, bold=True):
    bold_open_tag = None
    bold_close_tag = None
    if bold:
        bold_open_tag = '<b>'
        bold_close_tag = '</b>'
    return f'<font color="{text_color}">{bold_open_tag}{text}{bold_close_tag}</font>'

frame = {
    'BorderWidth': 3,
    'BorderColor': WHITE_BORDER,
    'CornerRadius': 10
}

information_button = {
    "Columns": 3,
    "Rows": 1,
    "BgColor": MILKY_COLOR,
    "ActionType": "reply",
    "ActionBody": "Information",
    "Text": format_text_with_color('❓ Інформація'),
    "TextSize": "large",
    "TextHAlign": "center",
    "TextVAlign": "middle",
    "Frame": frame
}

menu_button = {
    "Columns": 6,
    "Rows": 1,
    "ActionType": "reply",
    "ActionBody": "Menu",
    "Text": format_text_with_color('🔵 Меню', text_color=MILKY_COLOR),
    "TextSize": "large",
    "TextVAlign": "middle",
    "TextHAlign": "center",
    "BgColor": BORDO_COLOR,
    "Frame": frame
}

to_site_button = {
    "Columns": 6,
    "Rows": 1,
    "BgColor": MILKY_COLOR,
    "ActionType": "open-url",
    "ActionBody": "https://cosmy.com.ua/",
    "Text": format_text_with_color('🔍 Перейти на сайт'),
    "Silent": True,
    "TextSize": "large",
    "TextHAlign": "center",
    "TextVAlign": "middle",
    "Frame": frame
}


share_phone_keyboard = {
    "Type": "keyboard",
    "DefaultHeight": False,
    "Buttons": [
        {
            "Columns": 6, 
            "Rows": 1, 
            "BgColor": MILKY_COLOR,
            "ActionType": "share-phone",
            "ActionBody": "Share phone number",
            "Text": format_text_with_color('📞 Share Phone Number'),
            "TextSize": "large",
            "TextVAlign": "middle",
            "TextHAlign": "center",
            "TextOpacity": 100, 
            "BgLoop": True,
            "Frame": frame
        }
    ],
}

main_keyboard = {
    "Type": "keyboard",
    "DefaultHeight": True,
    # "BgColor": MAIN_KEYBOARD_BG_COLOR, 
    
    "Buttons": [
        {
            "Columns": 6,
            "Rows": 1,
            "BgColor": MILKY_COLOR, 
            "ActionType": "open-url",
            "ActionBody": "viber://chat?number=+380733175443",
            "Text": format_text_with_color("💪 Консультація"),
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle",
            "Frame": frame
            
        },
        {
            "Columns": 6,
            "Rows": 1,
            "BgColor": MILKY_COLOR,
            "ActionType": "reply",
            "ActionBody": "ContactCenter",
            "Text": format_text_with_color("📞 Контактний центр"),
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle",
            "Frame": frame
        },
        {
            "Columns": 6,
            "Rows": 1,
            "BgColor": MILKY_COLOR,
            "ActionType": "reply",
            "ActionBody": "MyOrder",
            "Text": format_text_with_color("🎁 Моє замовлення"),
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle",
            "Frame": frame
        },
        {
            "Columns": 6,
            "Rows": 1,
            "BgColor": MILKY_COLOR,
            "ActionType": "reply",
            "ActionBody": "OrderHistory",
            "Text": format_text_with_color("📄 Історія замовлень"),
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle",
            "Frame": frame
        },
        to_site_button,
        information_button,
        {
            "Columns": 3,
            "Rows": 1,
            "BgColor": MILKY_COLOR,
            "ActionType": "reply",
            "ActionBody": "Settings",
            "Text": format_text_with_color("⚙️ Налаштування"),
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle",
            "Frame": frame
        },
        
    ]    
}


contacts_keyboard = {
    "Type": "keyboard",
    "DefaultHeight": False,
    "Buttons": [
        {
            "Columns": 3,
            "Rows": 1,
            "BgColor": MILKY_COLOR,
            "ActionType": "reply",
            "ActionBody": "Contacts",
            "Text": format_text_with_color("📞 Контакти"),
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle",
            "Frame": frame
        },
        information_button,
        {
            "Columns": 3,
            "Rows": 1,
            "BgColor": MILKY_COLOR,
            "ActionType": "open-url",
            "ActionBody": "https://www.instagram.com/cosmy/",
            "Text": format_text_with_color("📸 Інстаграм"),
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle",
            "Frame": frame
        },
        {
            "Columns": 3,
            "Rows": 1,
            "BgColor": MILKY_COLOR,
            "ActionType": "open-url",
            "ActionBody": "https://cosmy.com.ua/",
            "Text": format_text_with_color("🔍 Наш сайт"),
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle",
            "Frame": frame
        },
        menu_button,
    ]
}


map_keyboard = {
    "Type": "keyboard",
    "DefaultHeight": False,
    "Buttons": [
        {
            "Columns": 6,
            "Rows": 1,
            "BgColor": MILKY_COLOR,  
            "ActionType": "reply",
            "ActionBody": "Map",
            "Text": format_text_with_color("🗺️ Переглянути карту"),
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle",
            "Frame": frame
        },
        menu_button
    ]
}

menu_keyboard = {
    "Type": "keyboard",
    "DefaultHeight": False,
    "Buttons": [
        menu_button
    ]

}

settings_keyboard = {
    "Type": "keyboard",
    "DefaultHeight": False,
    "Buttons": [
        {
            "Columns": 6,
            "Rows": 1,
            "ActionType": "reply",
            "ActionBody": "ChangePhoneNumber",
            "Text": format_text_with_color("🔄 Змінити номер телефону"),
            "TextSize": "large",
            "TextVAlign": "middle",
            "TextHAlign": "center",
            "BgColor": MILKY_COLOR,
            "Frame": frame
        },
        menu_button,
    ]
}

rich_media_links_part1 = {
    "Type": "rich_media",
    "ButtonsGroupColumns": 6,  
    "ButtonsGroupRows": 5,     
    "BgColor": WHITE_BORDER,      
    "Buttons": [
        {
            "Columns": 6,
            "Rows": 1,
            "ActionType": "open-url",
            "ActionBody": "https://cosmy.com.ua/dostavka-i-oplata-ua",
            "Text": format_text_with_color("🚚 Доставка і оплата"),
            "TextSize": "large",
            "TextVAlign": "middle",
            "TextHAlign": "center",
            "BgColor": MILKY_COLOR,
            "Silent": True,
            "OpenURLType": "internal",
            "Frame": {
                'BorderWidth': 1,
                'BorderColor': WHITE_BORDER,
            }
        },
        {
            "Columns": 6,
            "Rows": 1,
            "ActionType": "open-url",
            "ActionBody": "https://cosmy.com.ua/cosmy-club-ua",
            "Text": format_text_with_color("🌟 Космі клаб"),
            "TextSize": "large",
            "TextVAlign": "middle",
            "TextHAlign": "center",
            "BgColor": MILKY_COLOR,
            "Silent": True,
            "OpenURLType": "internal",
            "Frame": {
                'BorderWidth': 1,
                'BorderColor': WHITE_BORDER,
            }
        },
        {
            "Columns": 6,
            "Rows": 1,
            "ActionType": "open-url",
            "ActionBody": "https://cosmy.com.ua/sertifikati-jakosti-ua",
            "Text": format_text_with_color("📃 Сертифікати якості"),
            "TextSize": "large",
            "TextVAlign": "middle",
            "TextHAlign": "center",
            "BgColor": MILKY_COLOR,
            "Silent": True,
            "OpenURLType": "internal",
            "Frame": {
                'BorderWidth': 1,
                'BorderColor': WHITE_BORDER,
            }
        },
        {
            "Columns": 6,
            "Rows": 1,
            "ActionType": "open-url",
            "ActionBody": "https://cosmy.com.ua/podarochnie-sertifikati-ua",
            "Text": format_text_with_color("🎁 Подарункові сертифікати"),
            "TextSize": "large",
            "TextVAlign": "middle",
            "TextHAlign": "center",
            "BgColor": MILKY_COLOR,
            "Silent": True,
            "OpenURLType": "internal",
            "Frame": {
                'BorderWidth': 1,
                'BorderColor': WHITE_BORDER,
            }
        },
        {
            "Columns": 6,
            "Rows": 1,
            "ActionType": "open-url",
            "ActionBody": "https://cosmy.com.ua/pro-magazin-ua",
            "Text": format_text_with_color("❤️ Наш космі"),
            "TextSize": "large",
            "TextVAlign": "middle",
            "TextHAlign": "center",
            "BgColor": MILKY_COLOR,
            "Silent": True,
            "OpenURLType": "internal",
            "Frame": {
                'BorderWidth': 1,
                'BorderColor': WHITE_BORDER,
            }
        },
    ]
}

rich_media_links_part2 = {
    "Type": "rich_media",
    "ButtonsGroupColumns": 6,  
    "ButtonsGroupRows": 4,    
    "BgColor": WHITE_BORDER,    
    "Buttons": [
        {
            "Columns": 6,
            "Rows": 1,
            "ActionType": "open-url",
            "ActionBody": "https://cosmy.com.ua/povernennja-tovaru-ua",
            "Text": format_text_with_color("📄 Політика конфіденційності"),
            "TextSize": "large",
            "TextVAlign": "middle",
            "TextHAlign": "center",
            "BgColor": MILKY_COLOR,
            "Silent": True,
            "OpenURLType": "internal",
            "Frame": {
                'BorderWidth': 1,
                'BorderColor': WHITE_BORDER,
            }
        },
        {
            "Columns": 6,
            "Rows": 1,
            "ActionType": "open-url",
            "ActionBody": "https://cosmy.com.ua/umovi-zgodi-ua",
            "Text": format_text_with_color("🤝 Публічна угода"),
            "TextSize": "large",
            "TextVAlign": "middle",
            "TextHAlign": "center",
            "BgColor": MILKY_COLOR,
            "Silent": True,
            "OpenURLType": "internal",
            "Frame": {
                'BorderWidth': 1,
                'BorderColor': WHITE_BORDER,
            }
        },
        {
            "Columns": 6,
            "Rows": 1,
            "ActionType": "open-url",
            "ActionBody": "https://cosmy.com.ua/blog-ua",
            "Text": format_text_with_color("📚 Блог"),
            "TextSize": "large",
            "TextVAlign": "middle",
            "TextHAlign": "center",
            "BgColor": MILKY_COLOR,
            "Silent": True,
            "OpenURLType": "internal",
            "Frame": {
                'BorderWidth': 1,
                'BorderColor': WHITE_BORDER,
            }
        },
        {
            "Columns": 6,
            "Rows": 1,
            "ActionType": "reply",
            "ActionBody": "Menu",
            "Text": format_text_with_color("🔵 Меню"),
            "TextSize": "large",
            "TextVAlign": "middle",
            "TextHAlign": "center",
            "BgColor": MILKY_COLOR,
            "Silent": True,
            "Frame": {
                'BorderWidth': 1,
                'BorderColor': WHITE_BORDER,
            }
        }
    ]
}

no_orders_keyboard = {
    "Type": "keyboard",
    "DefaultHeight": False,
    "BgColor": WHITE_BORDER,
    "Buttons": [
        to_site_button,
        menu_button
    ]
}

next_page = {
    "Columns": 1,
    "Rows": 1,
    "BgColor": MILKY_COLOR,
    "ActionType": "none",
    "ActionBody": "none",
    "Text": format_text_with_color('>'),
    "TextSize": "large",
    "TextHAlign": "center",
    "TextVAlign": "middle",
    "Frame": frame

}


rich_media_indexing = {
    "Type": "keyboard",
    "ButtonsGroupColumns": 1,  
    "ButtonsGroupRows": 2,
    "Buttons": [
        next_page,
        next_page
    ]
}
