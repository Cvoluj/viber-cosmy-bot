from dataclasses import dataclass
import json
import os
from threading import Lock


@dataclass
class Waiter:
    recieved_message: str | None
    sender_id: int | str | None = None
    is_waiting: bool = True

WAITERS_FILE = "waiters.json"
lock = Lock()


def load_waiters():
    if os.path.exists(WAITERS_FILE):
        with open(WAITERS_FILE, "r") as file:
            return json.load(file)
    return {}

def save_waiters(waiters):
    with lock:
        with open(WAITERS_FILE, "w") as file:
            json.dump(waiters, file)

def update_waiter(sender_id, waiter):
    waiters = load_waiters()
    waiters[sender_id] = waiter
    save_waiters(waiters)

def get_waiter(sender_id):
    waiters = load_waiters()
    return waiters.get(sender_id)


