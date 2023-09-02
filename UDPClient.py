from socket import *

if __name__ == "__main__":
    server_name = '127.0.0.1'
    server_port = 5005
    dietime = 'die vremya'      
    client_socket = socket(AF_INET, SOCK_DGRAM)
    message = str(dietime).encode()
    client_socket.sendto(message, (server_name, server_port))

    modified_message, server_address = client_socket.recvfrom(2048)
    modified_message = modified_message.decode()
    print(modified_message)
    client_socket.close()
