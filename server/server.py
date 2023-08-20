import socket
import ssl

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket Succesfully Created")
server.bind(('127.0.0.1', 12345))
server.listen(5)

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='server.crt', keyfile='server.key')
print(f'socket binded to port{12345}')
print("Server listening...")

while True:
    client, addr = server.accept()
    print("Got Connection from", addr)
    ssl_client = context.wrap_socket(client, server_side=True)
    data = ssl_client.recv(1024)
    print(f"Received: {data.decode()}")
    ssl_client.send("Hello from server!".encode())
    ssl_client.close()
