from urllib.request import Request
import requests


request_from_user1 = {
    "url": "localhost/home/",
    "method": "GET",
    "data": {"попытка входа": 1},
    "timeout": 3000,
    "headers": {
        "Authorization": 'Bearer admin qwerty12345',
    },
}

request_from_user2 = {
    "url": "localhost/",
    "method": "POST",
    "data": {"попытка входа": 1},
    "timeout": 3000,
    "headers": {},

}

users_login_password = request_from_user1["headers"]["Authorization"]
right_login_password = request_from_user1["headers"]["Authorization"]
wrong_login_password = False


class AuthError(Exception):
    def __init__(self, exception: str):
        self.exception = exception

    def return_error(self):
        return f'ERROR: {self.exception}'



def decorator(func):
    def wrapper():
        func()
        try:
            if users_login_password == wrong_login_password:
                print("Проверка пройдена, вы успешно авторизовались!")
            else:
                raise AuthError(exception="wrong login or password")
            return "error"
        except AuthError as error:
            error = error.return_error()
            print(error)

    return wrapper

def some_func():
    print("Проверка данных...")

f = decorator(some_func)
f()



if users_login_password == right_login_password:
    class RequestManager(Request):
        response = requests.get(url="localhost/home/")
        print(response.content)
        response = requests.post(url="localhost/home/")


