import requests


from settings import settings


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0'
}


def synchronize_user(user_id, phone):
    api_url = f"https://cosmy.com.ua/index.php?route=api/v2/customer/createOrUpdateViber&api_token={settings.api_token}"
    data = {
            'telephone': phone,
            'viber_id': user_id
        }
    response = requests.post(api_url, data=data, headers=headers)
    if response.status_code == 200:
        print(f"User {user_id} synchronized successfully with phone {phone}")
    else:
        print(f"Failed to synchronize user {user_id}. Status code: {response.status_code}")


def delete_user_from_messenger(phone):
    messenger="viber"
    api_url = f"https://cosmy.com.ua/index.php?route=api/v2/customer/deleteMessenger&api_token={settings.api_token}"
    data = {
        'telephone': phone,
        'messenger': messenger
    }
    response = requests.post(api_url, data=data, headers=headers)
    if response.status_code == 200:
        print(f"User with phone {phone} removed from {messenger} successfully.")
    else:
        print(f"Failed to remove user with phone {phone} from {messenger}. Status code: {response.status_code}, Response: {response.text}")