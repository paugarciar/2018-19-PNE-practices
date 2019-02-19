import socket

PORT = 8080
IP = "212.128.253.70"
MAX_OPEN_REQUEST = 5


def process_client(cs):

    # reading message from the client
    msg = cs.recv(2048).decode("utf-8")  # maximum length that we want to receive

    print("Message from the client: {}".format(msg))
    # sending the message back to the client (because we are an echo server)
    cs.send(str.encode(msg))

    cs.close()


# Create a socket for connecting to the clients
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}".format(serversocket))


while True:

    print("waiting for connections at: {}, {}".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()
    # waits the client to be connected, then returns IP and client socket

    # Process the client request
    print("attending client: {}".format(address))

    process_client(clientsocket)
