# Program to print client messages in a different color
# and closing the server when the client writes EXIT

import socket
import termcolor
PORT = 8081
IP = "192.168.1.106"
MAX_OPEN_REQUEST = 5
ex = [0]  # this list will be modified to close the loop


def process_client(cs):

    # reading message from the client
    msg = cs.recv(2048).decode("utf-8")  # translating the message
    termcolor.cprint(msg, "yellow")  # printing it in yellow

    if msg == "EXIT":
        ex.append(1)  # add an element that changes length to 2

    # sending the message back to the client (because we are an echo server)
    cs.send(str.encode(msg))
    cs.close()


# Create a socket for connecting to the clients
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}".format(serversocket))

on = True
while on:

    print("waiting for connections at: {}, {}".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()
    # waits the client to be connected, then returns IP and client socket

    # Process the client request
    print("attending client: {}".format(address))

    process_client(clientsocket)
    if len(ex) == 2:
        on = False  # going out of the loop
