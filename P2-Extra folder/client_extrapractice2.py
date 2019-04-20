# Client that asks the user for a sequence and send it to the server
import socket

# Loop that goes on asking for entering new sequences
while True:
    # we want to create a socket for communicating with the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("socket created")

    PORT = 8081
    IP = "172.20.10.6"

    s.connect((IP, PORT))

    # converting the strings into binary code
    s.send(str.encode(input("Please insert a sequence: ")))

    # When the server sends the response, the client decodes it and prints it
    msg = s.recv(2048).decode("utf-8")
    print("Message from the server:")
    print(msg)

    s.close()
