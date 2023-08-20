import socket
import ssl

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("Socket Succesfully Created")
    server.bind(('127.0.0.1', 12345))
    server.listen(5)

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile='server.crt', keyfile='server.key')
    context.verify_mode = ssl.CERT_REQUIRED  # Require client certificate
    context.load_verify_locations(cafile='server.crt')  # Load CA certificates for client verification

    print(f'Socket binded to port {12345}')
    print("Server listening...")

    while True:
        client, addr = server.accept()
        print("Got Connection from", addr)
        ssl_client = context.wrap_socket(client, server_side=False)
        
        try:
            # Verify client certificate
            ssl_client.do_handshake()
            peer_cert = ssl_client.getpeercert()
            if ssl.match_hostname(peer_cert, '127.0.0.1'):
                print("Client authenticated:", peer_cert)
                data = ssl_client.recv(1024)
                print(f"Received: {data.decode()}")
                ssl_client.send("Hello from server!".encode())
            else:
                print("Client authentication failed: Invalid hostname")
        except ssl.SSLError as e:
            print("Client authentication failed:", e)
        
        ssl_client.close()

if __name__ == "__main__":
    main()
