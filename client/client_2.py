import socket
import ssl

context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_client = context.wrap_socket(client, server_hostname='127.0.0.1')
ssl_client.connect(('127.0.0.1', 12345))

# Read the MP3 file
with open('1230.mp3', 'rb') as mp3_file:
    mp3_data = mp3_file.read()

# Send the MP3 data
ssl_client.sendall(mp3_data)
print("\nFile Shared\n")
ssl_client.close()
