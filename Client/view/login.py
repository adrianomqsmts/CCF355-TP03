import json
import controller.client as clt


def loginview():
    name = input('Nome: ')
    password = input('Password: ')

    response = _login(name, password)

    if response:
        print('Bem-vindo {}'.format(response['name']))
        return response
    else:
        print('Nome e/ou senha inválidos')
        return None


def _login(name, password):
    data = {
        'function': 0,
        'name': name,
        'password': password
    }

    response = clt.client(data=data)  # A resposta possui um campo response com TRUE OU FALSO

    if response['response']:
        return response
    else:
        return 0
