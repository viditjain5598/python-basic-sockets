import socket
import select

HEADER_LEN = 10

IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))
server_socket.listen(5)

socket_list = [server_socket]
clients = {}

print(f"listening to {IP}:{PORT} for connections")

def recieve_message(client_socket):
    try:
        msg_hdr = client_socket.recv(HEADER_LEN)
        if not len(msg_hdr):
            return False
        msg_len = int(msg_hdr.decode("utf-8").strip())
       # msg = client_socket.recv(msg_len)
        return {'header':msg_hdr, 'data':client_socket.recv(msg_len)}

    except:
        return False




