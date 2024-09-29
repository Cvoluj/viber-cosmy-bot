import requests

def send_location_message(user_id, viber_auth_token, lat, lon, address="Your Address Here"):
    url = "https://chatapi.viber.com/pa/send_message"
    
    payload = {
        "receiver": user_id,
        "type": "location",
        "location": {
            "lat": lat,
            "lon": lon,
            "address": address 
        }
    }
    
    headers = {
        "Content-Type": "application/json",
        "X-Viber-Content-Type": "application/json",
        "Authorization": viber_auth_token
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        print("Location message sent successfully!")
    else:
        print(f"Failed to send location message: {response.text}")