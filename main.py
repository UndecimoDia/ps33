import requests

NUM = '0935733333'
AUTH_LINK = 'https://admin.pizza33.ua/login/'


def try_psw(psw):
    data = {'phone':NUM,
            'password': psw}
    res = requests.post(AUTH_LINK, data=data)
    res = res.json()
    print(res['message'])


try_psw('12345')