# Server that prints the reverse complement sequence received from the client

import socket

# Configure the Server's IP and PORT
PORT = 8081
IP = "192.168.1.20"
MAX_OPEN_REQUESTS = 5

# Counting the number of connections
number_con = 0

# Creating an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((IP, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        # Another connection
        number_con += 1

        # Print the connection number
        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        # Decoding and printing the message from the client
        msg = clientsocket.recv(2048).decode("utf-8")
        print("Message from client: {}".format(msg))

        clientsocket.close()

# Dealing with errors
except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()
