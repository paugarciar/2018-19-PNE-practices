# Client that can request several operations (len, complement, reverse, count, percentage) about a DNA sequence
import socket

# SERVER IP, PORT
IP = "192.168.1.20"
PORT = 8080

# Create the socket
while True:
    # The client write data and then it connects to the server and send it quickly
    msg = input('Please enter a message with each line separated by \\n: ')

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the request message to the server
    s.send(str.encode(msg))

    # Receive the servers response
    response = s.recv(2048).decode()

    # Print the server's response
    print("Response: {}".format(response))

    s.close()
