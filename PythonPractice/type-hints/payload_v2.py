from typing import TypedDict


class User(TypedDict):
    name: str
    email: str


def print_user(user: User) -> None:
    print(f"{user['name']} <{user['email']}>")


user: User = {"name": "Fadel", "email": "fadel@gmail.com"}

print_user(user)
