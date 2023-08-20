import socket
import ssl

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='server.crt', keyfile='server.key')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 12345))
server.listen(5)

while True:
    print("Listening....")
    client, addr = server.accept()
    ssl_client = context.wrap_socket(client, server_side=True)


    mp3_data = b''
    while True:
        chunk = ssl_client.recv(1024)
        if not chunk:
            break
        mp3_data += chunk

    with open('1230.mp3', 'wb') as received_file:
        received_file.write(mp3_data)
    print("File received")
    ssl_client.close()
