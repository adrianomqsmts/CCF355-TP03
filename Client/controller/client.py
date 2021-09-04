import socket
import json
import view


def client(host='localhost', port=8082, data=None):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Criando um socket TCP
    server_address = (host, port)  # Conectar ao servidor
    # print("Conectando ao servidor {} pela porta {}".format(server_address[0], server_address[1]))
    sock.connect(server_address)

    try:  # Enviar dados ao servidor
        if data:  # Verificar se Existe uma mensagem
            #  converter dicionário para string
            message = json.dumps(data)
            # print("Enviando mensagem ao servidor: {}".format(message))
            sock.sendall(message.encode('utf-8'))  # Enviar mensagem para o servidor
            response = sock.recv(8000)  # Receber a resposta do servidor
            response = json.loads(response)  # Converter sring para dicionário
            # print("Mensagem recebida: {}".format(response))
            return response
        else:
            print("Não tem dados para enviar ao servidor")
    except socket.error as e:
        print("Socket error: %s" % str(e))
    except Exception as e:
        print("Other exception: %s" % str(e))
    finally:
        #  print("Fechando a conexão com o servidor")
        sock.close()  # Encerrar a conexão do socket
