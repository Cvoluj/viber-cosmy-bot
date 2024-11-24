

def format_order_data(order_data):
    order = order_data['order']
    details = {
        "Номер замовлення": f"*{order.get('order_id', 'Немає даних')}*",
        "Сума замовлення": f"*{order.get('total', 'Немає даних')}*",
        "Статус замовлення": f"*{order.get('order_status', 'Немає даних')}*",
        "Дата замовлення": f"*{order.get('date_added', 'Немає даних')}*",
        "Спосіб доставки": f"*{order.get('shipping_method', 'Немає даних')}*",
        "Місто": f"*{order.get('payment_city', 'Немає даних')}*",
        "Адреса": f"*{order.get('payment_address_1', 'Немає даних')}*",
        "Товари у замовленні": [
            f"*{product.get('product_info', {}).get('name', 'Немає даних')}*"
            for product in order.get('order_products', [])
        ]
    }
    return details
