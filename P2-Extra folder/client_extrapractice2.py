import socket

while True:
    # we want to create a socket for communicating with the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("socket created")

    PORT = 8080
    IP = "192.168.1.34"

    s.connect((IP, PORT))

    # converting the strings into binary code
    s.send(str.encode(input("Please insert a sequence: ")))

    msg = s.recv(2048).decode("utf-8")
    print("Message from the server:")
    print(msg)

    s.close()
