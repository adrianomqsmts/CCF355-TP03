import json
import controller.client as clt


def singinview():
    name = input('Nome: ')
    password = input('Password: ')

    response = _singin(name, password)

    if response:
        print('Conta criada com sucesso.')
    else:
        print('Não foi possível criar a conta, possívelmente o nome já existe')


def _singin(name, password):
    data = {
        'function': 6,
        'name': name,
        'password': password
    }

    response = clt.client(data=data)

    if response['response']:
        return response
    else:
        return 0
