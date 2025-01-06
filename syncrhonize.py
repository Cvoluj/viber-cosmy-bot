import sqlite3
import requests
from settings import settings

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0'}

def login():
    data = {
        'username': (None, "Telegram"),
        'key': (None, settings.cosmy_api_key),
    }
    try:
        response = requests.post('https://cosmy.com.ua/index.php?route=api/login', files=data, headers=headers)
        response.raise_for_status()
        login_data = response.json()
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

def synchronize_users(api_token):
    conn = sqlite3.connect('viber_users.db')
    cursor = conn.cursor()

    cursor.execute("SELECT user_id, number FROM user")
    users = cursor.fetchall()

    api_url = f"https://cosmy.com.ua/index.php?route=api/v2/customer/createOrUpdateViber&api_token={api_token}"

    for user in users:
        user_id, phone = user
        data = {
            'telephone': phone,
            'viber_id': user_id
        }
        response = requests.post(api_url, data=data, headers=headers)
        if response.status_code == 200:
            print(f"User {user_id} synchronized successfully.")
        else:
            print(f"Failed to synchronize user {user_id}. Status code: {response.status_code}")

    conn.close()

if __name__ == "__main__":
    api_token = login()
    if api_token:
        synchronize_users(api_token)
    else:
        print("Не вдалося отримати api_token. Синхронізація користувачів не виконана.")