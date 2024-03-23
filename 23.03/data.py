import dataclasses
from dataclasses import dataclass

@dataclasses
class User:
    first_name: str = None,
    last_name: str = None,
    phone_number: str = None