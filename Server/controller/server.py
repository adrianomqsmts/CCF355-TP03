import model.usuario as user
import model.album as album
import model.figura as figure
import json
import socket
from threading import Thread
from datetime import datetime


class Servidor:

    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Criando o socket TCP
        self._tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start(self):
        endpoint = (self._host, self._port)
        try:
            self._tcp.bind(endpoint)  # Ligar o Socket à porta
            self._tcp.listen(5)  # Número máximo de clientes permitidos na fila
            print('Servidor iniciado em {}:{}'.format(self._host, self._port))
            while True:  # Recebendo Mensagens dos clientes
                try:
                    con, client = self._tcp.accept()
                    # Thread(target=self._service, args=(con, client))
                    self._service(con, client)
                except Exception as e:
                    print("Erro ao receber/enviar a mensagem do cliente: ", e.args)
        except Exception as e:
            print("Erro ao iniciar o servidor", e.args)

    def _service(self, con, client):
        try:  # Comunicando com o cliente
            msg = con.recv(10000)  # Tamanho máximo da mensagem em bits
            msg = json.loads(msg)  # Convertendo os bytes para dicionário
            print(client, ' -> Solicitação: ', msg)
            function = msg['function']   # Pegando o contexto da mensagem
            output = self._controller(function=function, data=msg)  # atribuindo a solicitação
            print(client, ' <- Resposta: ', output)
            con.send(output.encode())  # Resposta ao cliente
            con.close()  # fehcando a conexão com o cliente
        except OSError as e:
            print("Erro na conexao", client, ":", e.args)

    def _controller(self, function, data):
        if function == 0:  # Login msg = (action, name, password, date) - Verificar sorteio diário
            name = data['name']
            password = data['password']
            # strdate = now.split(" ")[0]
            resp = self._login(name, password)
            return resp
        elif function == '1':  # Vender Cartas msg = (action, idUser, idCarta, quantidade)
            return 0
        elif function == 2:  # Comprar Carta msg = (action, idUser, idCarta, quantidade)
            idUser = data['idUser']
            resp = self._buy(idUser)
            return resp
        elif function == '3':  # Trocar Carta msg = (action, idUser, idCarta, quantidade)
            return 0
        elif function == '4':  # Anunciar Carta msg = (action, idUser, idCarta, quantidade)
            return 0
        elif function == '5':  # Atualiar Cadastro msg = (action, idUser, name, password)
            return 0
        elif function == 6:  # Criar Conta msg = (action, name, password)
            name = data['name']
            password = data['password']
            resp = self._create(name, password)
            return resp
        elif function == 7:  # Ver Album msg = (action, idUser)
            idUser = data['idUser']
            resp = self._album(idUser)
            return resp
        else:  # Mensagem inválida
            return -1
        return 0

    def _login(self, name, password):

        database = user.login(name=name, password=password)

        if database:
            result = {
                'response': True,
                'idUser': database['idUser'],
                'name': database['name'],
                'password': database['password'],
                #'idLastLogin' : result['idLastLogin']
            }
        else:
            result = {
                'response': False,
                'idUser': '',
                'name': '',
                'password': '',
                #'idLastLogin': ''
            }

        data = json.dumps(result)  # convertendo para dicionário
        return data

    def _create(self, name, password):
        database = user.create(name=name, password=password)
        if database:
            result = {
                'response': True,
            }
        else:
            result = {
                'response': False,
            }

        data = json.dumps(result)  # convertendo para dicionário
        return data

    def _album(self, idUser):
        database = album.show(id_user=idUser)
        if database:
            result = database
        else:
            result = {
                'response': False,
            }
        data = json.dumps(result)  # convertendo para dicionário
        return data

    def _buy(self, idUser):
        database = figure.buy(idUser)
        if database:
            result = database
        else:
            result = {
                'response': False,
            }
        data = json.dumps(result)  # convertendo para dicionário
        return data