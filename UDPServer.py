from socket import *
from datetime import datetime


if __name__ == "__main__":
    server_port = 5005
    try:
        server_socket = socket(AF_INET, SOCK_DGRAM)
        server_socket.bind(('', server_port))
        print("The server is ready to receive")
        while 1:
            message, client_address = server_socket.recvfrom(2048)
            message = message.decode()
            modified_message = str(datetime.now()).encode()
            server_socket.sendto(modified_message, client_address)
    except KeyboardInterrupt:
        server_socket.close()
 