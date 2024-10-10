# About

* This is Cosmy viber bot, which work as mirror of existing 
* Telegram Cosmy Bot. Main feature - fetch user orders by phone number.
* Python 3.11+

## Installation Guide
1. clone repository
2. cp .env.example .env
3. Write bot auth-token and api-token
```
AUTH_TOKEN=<your-viber-bot-token>
API_TOKEN=<cosmy-api-token>
```
4. cp viber.json.example viber.json
5. Write your server host and port into url variable
```
{
    "url": "<http://server_host:server_port>"
}
```
6. pip install -r requirements.txt
7. python migrations.py
8. python main.py
9. `curl -# -i -g -H "X-Viber-Auth-Token:<paste_your_auth_token_here" -d @viber.json -X POST https://chatapi.viber.com/pa/set_webhook -v`