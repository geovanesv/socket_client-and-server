from pickle import TRUE
import socket

# Obtenha o endereço IP do host local
IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "DISCONNECT"

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect(ADDR)
        print(f"[CONNECTED] Cliente conectado ao servidor em {IP}:{PORT}") 
    except:
        print('Error ao tentar se conectar com o servidor!!!')

    connected = True
    username = input('usuario: ')
    while connected:
        
        msg = input("> ")
        #enviando o username e a msg para o servidor
        client.send(f'<{username}> {msg}'.encode(FORMAT))

        if msg == DISCONNECT_MSG:
            connected = False
        else:
            #msg recebe a mensagem de confirmação enviada pelo servidor
            msg = client.recv(SIZE).decode(FORMAT)
            print(f"[SERVER]: {msg}")

if __name__ == "__main__":
    main()
