import json
import controller.client as clt


def albumview(user):
    response = _album(user)

    if response:
        print('\n ------------ ALBUM ------------------')
        print("NOME | RARIDADE | QUANTIDADE")
        for figure in response:
            print(figure['name'], '|', figure['rarity'], '|', figure['quantity'])
        print()
        return 1
    else:
        print('Lamentamos, mas não foi possível encontrar o álbum')
        return None


def _album(user):
    data = {
        'function': 7,
        'idUser': user['idUser']
    }

    response = clt.client(data=data)

    if 'response' in response:  # Se tiver o campo responde dentro da resposta, então houve algum tipo de erro
        return 0
    else:
        return response
