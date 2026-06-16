def print_user(user: dict) -> None:
    print(f"{user['name']} <{user['email']}>")


user = {"name": "Fadel", "email": "fadel@gmail.com"}

print_user(user)
