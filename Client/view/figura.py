import json
import controller.client as clt


def figureview(user):
    response = _figure(user)
    balance = response[3]
    del response[3]

    if response:
        print('\n ------------ Figurinhas Adquiridas ------------------')
        print("ID | NOME | RARIDADE | ")
        for figure in response:
            print(figure['idFigure'], '|', figure['name'], '|', figure['rarity'])
        print('seu novo saldo é de', balance, "moedas")
        print()
        return 1
    else:
        print('Não foi possivel fazer a compra saldo insuficiente')
        return None



def _figure(user):
    data = {
        'function': 2,
        'idUser': user['idUser']
    }

    response = clt.client(data=data)

    if 'response' in response:  # Se tiver o campo responde dentro da resposta, então houve algum tipo de erro
        return 0
    else:
        return response
