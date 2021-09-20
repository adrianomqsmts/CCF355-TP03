import json
import controller.client as clt


def singinview(name, password):
    # name = input('Nome: ')
    # password = input('Password: ')
    print(name, password)
    response = _singin(name, password)
    print(response)
    if response:
        print('Conta criada com sucesso.')
        return response
    else:
        print('Não foi possível criar a conta, possívelmente o nome já existe')
        return None


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
