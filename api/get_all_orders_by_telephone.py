import requests
from api.startup_login import startup_login
from settings import settings


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0'
}



def get_all_last_orders_by_telephone(telephone):
    try:
        if not settings.cosmy_api_token:
            raise ValueError("COSMY_API_TOKEN is None, could't use api") 
        url = f'https://cosmy.com.ua/index.php?route=api/order/getOrdersByTelephone&api_token={settings.cosmy_api_token}&telephone={telephone}&description=1'
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        response_json = response.json()
        error = response_json.get("error")
        if error is not None:
            print(f"{error}, updating api key")
            startup_login()
            get_all_last_orders_by_telephone(telephone)
        return response_json
    except requests.exceptions.RequestException as e:
        print(f"Error recieving all orders by telephone: {e}")
        return None
    except ValueError as e:
        print(e)
        return None