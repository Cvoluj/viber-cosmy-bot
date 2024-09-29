MAIN_KEYBOARD_BG_COLOR = "#A8DADC"
CONTACT_KEYBOARD_BG_COLOR = "#A8DADC"


information_button = {
    "Columns": 3,
    "Rows": 1,
    "BgColor": MAIN_KEYBOARD_BG_COLOR,
    "ActionType": "reply",
    "ActionBody": "Information",
    "Text": "❓ Інформація",
    "TextSize": "large",
    "TextHAlign": "center",
    "TextVAlign": "middle"
}

menu_button = {
    "Columns": 6,
    "Rows": 1,
    "ActionType": "reply",
    "ActionBody": "Menu",
    "Text": "🔵 <b>Меню</b>",
    "TextSize": "large",
    "TextVAlign": "middle",
    "TextHAlign": "center",
    "BgColor": MAIN_KEYBOARD_BG_COLOR
}

to_site_button = {
    "Columns": 6,
    "Rows": 1,
    "BgColor": MAIN_KEYBOARD_BG_COLOR,
    "ActionType": "open-url",
    "ActionBody": "https://cosmy.com.ua/",
    "Text": "🔍 Перейти на сайт",
    "Silent": True,
    "TextSize": "large",
    "TextHAlign": "center",
    "TextVAlign": "middle"
}


share_phone_keyboard = {
    "Type": "keyboard",
    "DefaultHeight": False,
    "Buttons": [
        {
            "Columns": 6,  # Збільшуємо кількість колонок, щоб кнопка займала ширше місце
            "Rows": 1,  # Збільшуємо висоту кнопки
            "BgColor": "#dddddd",  # Змінюємо колір фону на зелений для кращої видимості
            "ActionType": "share-phone",
            "ActionBody": "Share phone number",
            "Text": "📞 Share Phone Number",
            "TextSize": "large",
            "TextVAlign": "middle",
            "TextHAlign": "center",
            "TextOpacity": 100,  # Зробимо текст більш контрастним
            "BgLoop": True  # Щоб кнопка виглядала однорідно на будь-якому фоні
        }
    ],
}

main_keyboard = {
    "Type": "keyboard",
    "DefaultHeight": True,
    "BgColor": MAIN_KEYBOARD_BG_COLOR,  # Колір фону клавіатури
    "Buttons": [
        {
            "Columns": 6,
            "Rows": 1,
            "BgColor": MAIN_KEYBOARD_BG_COLOR,  # Колір кнопки
            "ActionType": "open-url",
            "ActionBody": "viber://chat?number=+380733175443",
            "Text": "💪 Консультація",
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle"
        },
        {
            "Columns": 6,
            "Rows": 1,
            "BgColor": MAIN_KEYBOARD_BG_COLOR,
            "ActionType": "reply",
            "ActionBody": "ContactCenter",
            "Text": "📞 Контактний центр",
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle"
        },
        {
            "Columns": 6,
            "Rows": 1,
            "BgColor": MAIN_KEYBOARD_BG_COLOR,
            "ActionType": "reply",
            "ActionBody": "MyOrder",
            "Text": "🎁 Моє замовлення",
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle"
        },
        {
            "Columns": 6,
            "Rows": 1,
            "BgColor": MAIN_KEYBOARD_BG_COLOR,
            "ActionType": "reply",
            "ActionBody": "OrderHistory",
            "Text": "📄 Історія замовлень",
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle"
        },
        to_site_button,
        information_button,
        {
            "Columns": 3,
            "Rows": 1,
            "BgColor": MAIN_KEYBOARD_BG_COLOR,
            "ActionType": "reply",
            "ActionBody": "Settings",
            "Text": "⚙️ Налаштування",
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle"
        }
    ]
}


contacts_keyboard = {
    "Type": "keyboard",
    "DefaultHeight": False,
    "BgColor": CONTACT_KEYBOARD_BG_COLOR,
    "Buttons": [
        {
            "Columns": 3,
            "Rows": 1,
            "BgColor": CONTACT_KEYBOARD_BG_COLOR,  # Колір кнопки
            "ActionType": "reply",
            "ActionBody": "Contacts",
            "Text": "📞 Контакти",
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle"
        },
        information_button,
        {
            "Columns": 3,
            "Rows": 1,
            "BgColor": CONTACT_KEYBOARD_BG_COLOR,
            "ActionType": "open-url",
            "ActionBody": "https://www.instagram.com/cosmy/",
            "Text": "📸 Інстаграм",
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle"
        },
        {
            "Columns": 3,
            "Rows": 1,
            "BgColor": CONTACT_KEYBOARD_BG_COLOR,
            "ActionType": "open-url",
            "ActionBody": "https://cosmy.com.ua/",
            "Text": "🔍 Наш сайт",
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle"
        },
        menu_button,
    ]
}


map_keyboard = {
    "Type": "keyboard",
    "DefaultHeight": False,
    "BgColor": CONTACT_KEYBOARD_BG_COLOR,
    "Buttons": [
        {
            "Columns": 6,
            "Rows": 1,
            "BgColor": CONTACT_KEYBOARD_BG_COLOR,  # Колір кнопки
            "ActionType": "reply",
            "ActionBody": "Map",
            "Text": "🗺️ Переглянути карту",
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle"
        },
        menu_button
    ]
}

menu_keyboard = {
    "Type": "keyboard",
    "DefaultHeight": False,
    "BgColor": CONTACT_KEYBOARD_BG_COLOR,
    "Buttons": [
        menu_button
    ]

}

settings_keyboard = {
    "Type": "keyboard",
    "DefaultHeight": False,
    "BgColor": CONTACT_KEYBOARD_BG_COLOR,
    "Buttons": [
        {
            "Columns": 6,
            "Rows": 1,
            "ActionType": "reply",
            "ActionBody": "ChangePhoneNumber",
            "Text": "🔄 Змінити номер телефону",
            "TextSize": "large",
            "TextVAlign": "middle",
            "TextHAlign": "center",
            "BgColor": CONTACT_KEYBOARD_BG_COLOR
        },
        menu_button,
    ]
}

rich_media_links_part1 = {
    "Type": "rich_media",
    "ButtonsGroupColumns": 6,  # Ширина групи кнопок
    "ButtonsGroupRows": 5,     # Висота групи кнопок
    "BgColor": "#DDFFCC",      # Колір фону повідомлення
    "Buttons": [
        {
            "Columns": 6,
            "Rows": 1,
            "ActionType": "open-url",
            "ActionBody": "https://cosmy.com.ua/dostavka-i-oplata-ua",
            "Text": "🚚 <b>Доставка і оплата</b>",
            "TextSize": "large",
            "TextVAlign": "middle",
            "TextHAlign": "center",
            "BgColor": "#E5F6DF",
            "Silent": True,
            "OpenURLType": "internal",
        },
        {
            "Columns": 6,
            "Rows": 1,
            "ActionType": "open-url",
            "ActionBody": "https://cosmy.com.ua/cosmy-club-ua",
            "Text": "🌟 <b>Космі клаб</b>",
            "TextSize": "large",
            "TextVAlign": "middle",
            "TextHAlign": "center",
            "BgColor": "#E5F6DF",
            "Silent": True,
            "OpenURLType": "internal",
        },
        {
            "Columns": 6,
            "Rows": 1,
            "ActionType": "open-url",
            "ActionBody": "https://cosmy.com.ua/sertifikati-jakosti-ua",
            "Text": "📃 <b>Сертифікати якості</b>",
            "TextSize": "large",
            "TextVAlign": "middle",
            "TextHAlign": "center",
            "BgColor": "#E5F6DF",
            "Silent": True,
            "OpenURLType": "internal",
        },
        {
            "Columns": 6,
            "Rows": 1,
            "ActionType": "open-url",
            "ActionBody": "https://cosmy.com.ua/podarochnie-sertifikati-ua",
            "Text": "🎁 <b>Подарункові сертифікати</b>",
            "TextSize": "large",
            "TextVAlign": "middle",
            "TextHAlign": "center",
            "BgColor": "#E5F6DF",
            "Silent": True,
            "OpenURLType": "internal",
        },
        {
            "Columns": 6,
            "Rows": 1,
            "ActionType": "open-url",
            "ActionBody": "https://cosmy.com.ua/pro-magazin-ua",
            "Text": "❤️ <b>Наш космі</b>",
            "TextSize": "large",
            "TextVAlign": "middle",
            "TextHAlign": "center",
            "BgColor": "#E5F6DF",
            "Silent": True,
            "OpenURLType": "internal",
        },
    ]
}

rich_media_links_part2 = {
    "Type": "rich_media",
    "ButtonsGroupColumns": 6,  # Ширина групи кнопок
    "ButtonsGroupRows": 4,     # Висота групи кнопок
    "BgColor": "#DDFFCC",      # Колір фону повідомлення
    "Buttons": [
        {
            "Columns": 6,
            "Rows": 1,
            "ActionType": "open-url",
            "ActionBody": "https://cosmy.com.ua/povernennja-tovaru-ua",
            "Text": "📄 <b>Політика конфіденційності</b>",
            "TextSize": "large",
            "TextVAlign": "middle",
            "TextHAlign": "center",
            "BgColor": "#E5F6DF",
            "Silent": True,
            "OpenURLType": "internal",
        },
        {
            "Columns": 6,
            "Rows": 1,
            "ActionType": "open-url",
            "ActionBody": "https://cosmy.com.ua/umovi-zgodi-ua",
            "Text": "🤝 <b>Публічна угода</b>",
            "TextSize": "large",
            "TextVAlign": "middle",
            "TextHAlign": "center",
            "BgColor": "#E5F6DF",
            "Silent": True,
            "OpenURLType": "internal",
        },
        {
            "Columns": 6,
            "Rows": 1,
            "ActionType": "open-url",
            "ActionBody": "https://cosmy.com.ua/blog-ua",
            "Text": "📚 <b>Блог</b>",
            "TextSize": "large",
            "TextVAlign": "middle",
            "TextHAlign": "center",
            "BgColor": "#E5F6DF",
            "Silent": True,
            "OpenURLType": "internal",
        },
        {
            "Columns": 6,
            "Rows": 1,
            "ActionType": "reply",
            "ActionBody": "Menu",
            "Text": "🔵 <b>Меню</b>",
            "TextSize": "large",
            "TextVAlign": "middle",
            "TextHAlign": "center",
            "BgColor": "#E5F6DF",
            "Silent": True,
        }
    ]
}

no_orders_keyboard = {
    "Type": "keyboard",
    "DefaultHeight": False,
    "BgColor": CONTACT_KEYBOARD_BG_COLOR,
    "Buttons": [
        to_site_button,
        menu_button
    ]
}