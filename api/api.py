import requests
from settings import settings


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0'
}


def startup_login():
    formdata = {
        "username": (None, "Telegram"),
        "key": (None, settings.cosmy_api_key)
    }

    try:
        response = requests.post(
            url="https://cosmy.com.ua/index.php?route=api/login",
            files=formdata,
            headers=headers
        )
        response.raise_for_status()
        api_token = response.json().get("api_token", None)
        if not api_token:
            return None
        
        settings.cosmy_api_token = api_token
        return api_token
    except requests.exceptions.HTTPError as e:
        print(e)

if __name__ == "__main__":
    token = startup_login()
    print(settings.cosmy_api_token)
