# programming our first client

import socket

# we want to create a socket for communicating with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("socket created")

PORT = 8080
IP = "212.128.253.64"

s.connect((IP, PORT))


# converting the strings into binary code
s.send(str.encode("hello from my client"))

msg = s.recv(2048).decode("utf-8")
print("message from the server:")
print(msg)

s.close()

print("The end")
