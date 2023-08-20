import socket
import ssl


context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile='ca.crt')
context.check_hostname = False 
context.verify_mode = ssl.CERT_NONE 
context.set_ciphers('DEFAULT@SECLEVEL=1') 
context.set_alpn_protocols(['http/1.1'])  

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ssl_client = context.wrap_socket(client, server_hostname='127.0.0.1')
ssl_client.connect(('127.0.0.1', 12345))

ssl_client.send("Hello from client!".encode())
data = ssl_client.recv(1024)
print(f"Received: {data.decode()}")

ssl_client.close()
