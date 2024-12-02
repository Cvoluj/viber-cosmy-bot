from dataclasses import dataclass

@dataclass
class Waiter:
    recieved_message: str | None
    sender_id: int | str | None = None
    is_waiting: bool = True


waiters: dict[str | int, Waiter | None] = {}
