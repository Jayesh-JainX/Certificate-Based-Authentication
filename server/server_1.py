import socket
import ssl

def receive_file(ssl_socket, filename):
    with open(filename, 'wb') as file:
        while True:
            data = ssl_socket.recv(4096)
            if not data:
                break
            file.write(data)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.80.160', 12345))
server.listen(5)

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='server.crt', keyfile='server.key')

print("Server listening...")
add,port=("192.168.80.79",12345)
while True:
    try:

        client, addr = server.accept()
        print("Got Connection from", addr)
        if(addr[0]==add):
            print("Unauthorized Access\n")
            continue
        else:
            ssl_client = context.wrap_socket(client, server_side=True)

            filename = ssl_client.recv(1024).decode()
            print(f"Receiving file: {filename}")
            receive_file(ssl_client, filename)
            print("File Received")
    except:
        print("Error") 
    ssl_client.close()

