import socket
import sys

def server_program(ip):
    port = 5000  

    server_socket = socket.socket()  
    server_socket.bind((ip, port))  

    server_socket.listen(2)
    conn, address = server_socket.accept()  
    print("Connection from: " + str(address))
    while True:
        
        data = conn.recv(1024).decode()
        if not data:
            
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode()) 

    conn.close()  


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python hola.py <ip_address>")
        sys.exit(1)
    ip_address = sys.argv[1]
    server_program(ip_address)