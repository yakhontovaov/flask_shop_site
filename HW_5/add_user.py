import requests


def add_user(name, email, password):
    url = 'http://127.0.0.1:8000/users/'

    new_user_data = {
        'name': name,
        'email': email,
        'password': password
    }

    response = requests.post(url, json=new_user_data)

    if response.status_code == 200:
        print("Пользователь успешно добавлен!")
    else:
        print("Произошла ошибка при добавлении пользователя:", response.text)


add_user("Новый пользователь 2", "newuser2@example.com", "securepassword2")
