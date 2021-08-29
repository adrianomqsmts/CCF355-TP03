import model.usuario as user
import json
import socket
from threading import Thread
from datetime import datetime


class Servidor:

    def __init__(self, host, port):
        self._host = host
        self._port = port
        # Criando o socket TCP
        self._tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start(self):
        endpoint = (self._host, self._port)
        try:
            # Ligar o Socket à porta
            self._tcp.bind(endpoint)
            # Número máximo de clientes permitidos na fila
            self._tcp.listen(5)
            print("Servidor iniciado em", self._host, ":", self._port)

            # Recebendo Mensagens dos clientes
            while True:
                con, client = self._tcp.accept()
                # Thread(target=self._service, args=(con, client))
                self._service(con, client)

        except Exception as e:
            print("Erro ao iniciar o servidor", e.args)

    def _service(self, con, client):
        print("Comunicando com o cliente", client)
        try:
            # Tamanho máximo da mensagem em bits
            msg = con.recv(6400)  # 1024
            # decodificando a mensagem
            data = json.loads(msg)
            function = data['function']
            # atribuindo a solicitação
            output = self._controller(function=function, data=data)
            # Resposta (debug)
            resp = 'confirmação de mensagem'
            con.send(output.encode())
            print("Enviada a mensagem ao cliente")
            con.close()
        except OSError as e:
            print("Erro na conexao", client, ":", e.args)

    def _controller(self, function, data):
        # Login msg = (action, name, password, date)
        # Verificar sorteio diário
        if function == '0':
            name = data['name']
            password = data['password']
            # strdate = now.split(" ")[0]
            resp = self._login(name, password)

            return resp

        # Vender Cartas msg = (action, idUser, idCarta, quantidade)
        elif function == '1':
            return 0

        # Comprar Carta msg = (action, idUser, idCarta, quantidade)
        elif function == '2':
            return 0
        # Trocar Carta msg = (action, idUser, idCarta, quantidade)
        elif function == '3':
            return 0
        # Anunciar Carta msg = (action, idUser, idCarta, quantidade)
        elif function == '4':
            return 0
        # Atualiar Cadastro msg = (action, idUser, name, password)
        elif function == '5':
            return 0
        # Criar Conta msg = (action, name, password)
        elif function == '6':
            return 0
        # Ver Album msg = (action, idUser)
        elif function == '7':
            return 0
        # Mensagem invalida
        else:
            return -1

        return 0

    def _login(self, name, password):
        #now = str(datetime.today().year) + '-' + str(datetime.today().month) + '-' + str(datetime.today().day)
        # Verifica se o usuário é valído para o sorteio diario
        #try:
        #    if strdate != now
        #        valid = 1
        #    else
        #        valid = 0
        #except:
        #    valid = 1
        #    if valid == 1:
        #        self._sorteio()

        result = user.login(name=name, password=password)

        if result:
            result = {
                'authenticated': True,
                'idUser': result['idUser'],
                'name': result['name'],
                'password': result['password'],
                #'idLastLogin' : result['idLastLogin']
            }
        else:
            result = {
                'authenticated': False,
                'idUser': '',
                'name': '',
                'password': '',
                #'idLastLogin': ''
            }

        data = json.dumps(result)
        return data


    def _sorteio(self):
        return 0





