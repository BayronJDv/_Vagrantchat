import socket
import sys

def client_program(server_ip):
    port = 5000  

    client_socket = socket.socket() 
    client_socket.connect((server_ip, port))  

    message = input(" -> ")  

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  
        data = client_socket.recv(1024).decode()  

        print('Received from server: ' + data)  

        message = input(" -> ")  

    client_socket.close()  


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python client.py <direccion_ip_servidor>")
        sys.exit(1)
    server_ip = sys.argv[1]
    client_program(server_ip)
