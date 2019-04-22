# Web server that gives the user access to three different html pages
# It has been programed using sockets
import socket
import termcolor

# IP AND PORT
IP = "192.168.1.20"
PORT = 8081
MAX_OPEN_REQUESTS = 5


# Processing the request received
def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Reading and decoding the client message
    msg = cs.recv(2048).decode("utf-8")

    # Separating the message in different parts
    lines_msg = msg.split("\n")  # Making a list of the lines of the message
    first_line = lines_msg[0].split(" ")  # Making a list of the first line of the message
    print()

    # Printing the complete request message in the server
    print("Request message: ")
    termcolor.cprint(msg, 'green')

    # Accessing to html pages
    if first_line[1] == "/":
        page = "index.html"
    elif first_line[1] == "/blue":
        page = "blue.html"
    elif first_line[1] == "/pink":
        page = "pink.html"
    else:
        page = "error.html"
    f = open(page, "r")
    content = f.read()  # Saving the contents in the variable content
    f.close()

    # Generating and sending the response message according to the request
    status_line = "HTTP/1.1 200 OK\r\n"
    header = "content-type: text/html\r\n"
    header += "content-length: {}\r\n".format(len(str.encode(content)))
    response_msg = status_line + header + "\r\n" + content
    cs.send(str.encode(response_msg))

    # Closing the socket
    cs.close()


# -- MAIN PROGRAM

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)
