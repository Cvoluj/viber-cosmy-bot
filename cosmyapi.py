import requests
from settings import settings

api_key = settings.api_token

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0'}

def login():
    data = {
        'username': (None, "Viber"),
        'key': (None, api_key),
    }
    try:
        response = requests.post('https://cosmy.com.ua/index.php?route=api/login', files=data, headers=headers)
        response.raise_for_status()
        login_data = response.json()

        if login_data == []:
            print('Хост не додано у довзолені')
            return None

        api_token = login_data.get('api_token')

        if api_token is None:
            error_message = login_data.get('error')
            print("Помилка: Не вдалося отримати api_token.")
            print(f"Деталі помилки: {error_message}")
            return None

        return api_token
    except requests.exceptions.RequestException as e:
        print(f"Помилка при логіні: {e}")
        return None

# Функція для отримання даних про замовлення за номером телефону
def get_last_order_by_telephone(api_token, telephone):
    try:
        url = f'https://cosmy.com.ua/index.php?route=api/order/lastOrderByTelephone&api_token={api_token}&telephone={telephone}'
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        order_data = response.json()
        return order_data
    except requests.exceptions.RequestException as e:
        print(f"Помилка при отриманні даних про замовлення: {e}")
        return None
    
    
def get_all_last_orders_by_telephone(api_token, telephone):
    try:
        url = f'https://cosmy.com.ua/index.php?route=api/order/getOrdersByTelephone&api_token={api_token}&telephone={telephone}&description=1'
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        orders_data = response.json()
        return orders_data
    except requests.exceptions.RequestException as e:
        print(f"Помилка при отриманні всіх замовлень: {e}")
        return None


def format_order_data(order_data):
    if order_data and 'order' in order_data:
        order = order_data['order']
        details = {
            "Номер замовлення": f"<b>{order.get('order_id', 'Немає даних')}</b>",
            "Сума замовлення": f"<b>{order.get('total', 'Немає даних')}</b>",
            "Статус замовлення": f"<b>{order.get('order_status', 'Немає даних')}</b>",
            "Дата замовлення": f"<b>{order.get('date_added', 'Немає даних')}</b>",
            "Спосіб доставки": f"<b>{order.get('shipping_method', 'Немає даних')}</b>",
            "Місто": f"<b>{order.get('payment_city', 'Немає даних')}</b>",
            "Адреса": f"<b>{order.get('payment_address_1', 'Немає даних')}</b>",
            "Товари у замовленні": [
                f"<b>{product.get('product_info', {}).get('name', 'Немає даних')}</b>"
                for product in order.get('order_products', [])
            ]
        }
        return details
    return None
