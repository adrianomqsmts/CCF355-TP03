import controller.client as clt
from tkinter import *
import view.login as vl
import view.singin as vs
import view.album as al
import view.figura as fg

# Press the green button in the gutter to run the script.


if __name__ == '__main__':  # clt.client()
    user = None
    print('Iniciando a aplicação...')
    while True:  # WHILE LOGIN
        option = input("1 - login | 2 - Criar conta | 0 - Sair: ")
        if option == '1':
            response = vl.loginview()
            if response:
                user = response  # Armazenar os dados do usuário
                while True:  # WHILE menu principal
                    option = input("1 - Álbum | 2 - Comprar | 3 - Vender | 4 - Trocar | 0 - Sair: ")
                    if option == '1':
                        response = al.albumview(user)
                        pass
                    elif option == '2':
                        opt = int(input("Você deseja confirmar a compra ? (custo 20 moedas)\n"
                                    "              1 - SIM | 2 - NÃO\n"))

                        if opt != 1:
                            continue
                        response = fg.figureview(user)
                    elif option == '3':
                        pass
                    elif option == '4':
                        pass
                    elif option == '0':
                        user = None  # limpar os dados do usuário
                        break
                    else:
                        print('Opção inválida, tente novamente...')
        elif option == '2':
            vs.singinview()
        else:
            break
