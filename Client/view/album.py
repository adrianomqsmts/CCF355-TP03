import json
import controller.client as clt


def albumview(user):
    response = _album(user)
    complete = response[1]['complete']
    special = response[2]
    del response[2]
    del response[1]
    if response[0]:
        print('\n ------------ ALBUM ------------------')
        print("ID | NOME | RARIDADE | QUANTIDADE")
        for figure in response[0]:
            print(figure['idFigure'], '|', figure['name'], '|', figure['rarity'], '|', figure['quantity'])
        if complete == 1:
            print('\nParabéns você completou o album e ganhou uma figurinha ESPECIAL exclusiva:\n')
            print("ID | NOME | RARIDADE")
            print(special['idFigure'], '|', special['name'], '|', special['rarity'])
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
