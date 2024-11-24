

def format_order_data(order_data):
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
