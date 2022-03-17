import socket
import threading

#função que pega o ip REAL da minha maquina que o servidor está rodando!!
IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
#formato utf-8 para codificar e descodificar as mensagens
FORMAT = "utf-8"
# a variavel DISCONNECT_MSG vai ser usada para o cliente desconectar-se do servidor 
DISCONNECT_MSG = "DISCONNECT"

''' 
a função handle_client estabelece a conexão do(s) cliente(s), recebe uma connection com
o ip e a porta do cliente,  
 a
'''
def handle_client(conn, addr):
    print(f"[Nova Conexão] {addr} conectado.")

    connected = True
    while connected:
        #MSG Recebe a mensagem enviada pelo cliente e decodifica no formato utf-8
        msg = conn.recv(SIZE).decode(FORMAT)
        if DISCONNECT_MSG in msg:
            connected = False

        print(f"[{addr}] : {msg}")
        '''
        quando a mensagem é recebida pelo servidor ele envia uma menagem de volta para o client
        com o texto MSG recebida informando que a mensagem chegou
        '''
        if msg != '':
            msg = "Msg recebida"
            conn.send(msg.encode(FORMAT))

    conn.close()

def main():
    print("O servidor está iniciando...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    '''LISTEM SERVE PARA ESPECIFICAR O QUANTAS CONEXÕES QUE O SEWRVIDOR PODE RECEBER
    Está sem um n° expecifico E assim pode ter multiploas conexões'''
    server.listen()
    print(f"O servidor está ouvindo {IP}:{PORT}")
    

    while True:
        '''
          server.accept vai aceitar a conexão requisitada pelo cliente nesse caso expecifico
          não tem validação,qualquer cliente pode se connectar com o  servidor!
        '''
        conn, addr = server.accept()
        '''
           Iniciar a thread que executa a função handle_client para estabelecer uma conexão com o cliente,
           que tem dois argumentos conn, e address que são informados em seguida args=(conn,addr)
        '''
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        #threading.activeCount(), está informando o número de conexões ativas
        print(f"[Conexões Ativas] {threading.activeCount() - 1}")

if __name__ == "__main__":
    main()
