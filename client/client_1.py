import socket
import ssl

def send_file(ssl_socket, filename):
    with open(filename, 'rb') as file:
        for data in file:
            ssl_socket.send(data)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile='ca.crt')
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

ssl_client = context.wrap_socket(client, server_hostname='127.0.0.1')
ssl_client.connect(('127.0.0.1', 12345))

filename = 'data.txt'
ssl_client.send(filename.encode())

send_file(ssl_client, filename)

ssl_client.close()
