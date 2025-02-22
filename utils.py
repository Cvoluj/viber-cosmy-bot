import re
from urllib.parse import urlparse


def format_order_data(order_data):
    def simplify_date(date_str):
        date = date_str.split()[0] if date_str else "Немає даних"
        parts = date.split("-") 
        return f"{parts[2]}.{parts[1]}.{parts[0]}" if len(parts) == 3 else "Не вдалось форматувати"

    order = order_data['order']
    details = {
        "Номер замовлення": f"*{order.get('order_id', 'Немає даних')}*",
        "Сума замовлення": f"*{order.get('total', 'Немає даних')}*",
        "Статус замовлення": f"*{order.get('order_status', 'Немає даних')}*",
        "Дата замовлення": f"*{simplify_date(order.get('date_added'))}*",
        "Спосіб доставки": f"*{order.get('shipping_method', 'Немає даних')}*",
        "Місто": f"*{order.get('payment_city', 'Немає даних')}*",
        "Адреса": f"*{order.get('payment_address_1', 'Немає даних')}*",
        "Товари у замовленні": [
            f"*{product.get('product_info', {}).get('name', 'Немає даних').strip()}*\n"
            for product in order.get('order_products', [])
        ],
        "Посилання":[
            f"{product.get('product_info', {}).get('url', '').strip()}\n"
            for product in order.get('order_products', [])
        ]
    }
    return details


def split_on_batches(iterable, batch: int):
    iterable_list = list(iterable)
    return [iterable_list[i:i + batch] for i in range(0, len(iterable_list), batch)]


def validate_url(message: str) -> str:
   
    url_pattern = re.compile(r'^(https?://)?([a-zA-Z0-9.-]+)(:[0-9]+)?(/.*)?$')
  
    if url_pattern.match(message):
    
        parsed = urlparse(message)
        if not parsed.scheme:
            message = f"https://{message}"  
        return message
    
    if ' ' not in message and '.' in message:
        return f"https://{message}"  
    
    return None

if __name__ == '__main__':
    print(validate_url("cosmy.com.ua/krem-dlja-chuvstvitelnoj-kozhi-lica-babor-skinovage-ua"))     
    print(validate_url("https://example.com"))  
    print(validate_url("not_a_url"))      
