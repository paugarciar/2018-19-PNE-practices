#code to prove conections between a server and a client
import socket

# this is the loop to go on chatting
connected = True
while connected:
    # we want to create a socket for communicating with the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("socket created")

    PORT = 8081
    IP = "212.128.253.67"

    s.connect((IP, PORT))

    # converting the strings into binary code
    s.send(str.encode(input("write a message: ")))

    s.close()