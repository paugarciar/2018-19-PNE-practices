import socket

PORT = 8081
IP = "192.168.1.34"
MAX_OPEN_REQUEST = 5


def first_line(fl):
    correct = True
    if len(fl) == 0:  # first line empty
        result = 'ALIVE'
    else:
        for letter in fl:
            if (letter != 'A') and (letter != 'C') and (letter != 'T') and (letter != 'G'):
                result = 'ERROR'  # there are letters that are not bases
                correct = False
        if correct:
            result = 'OK'  # all the letters are bases

    return result


def process_client(cs):

    # reading message from the client
    msg = cs.recv(2048).decode("utf-8")  # maximum length that we want to receive
    m_list = msg.split('\\n')  # divide the message into its different lines
    u_list = []  # m_list but with all letters in uppercase
    for element in m_list:
        element = element.upper()
        u_list.append(element)
    m = first_line(u_list[0])
    print("Message from the client: {}".format(msg))
    # sending the message back to the client (because we are an echo server)
    cs.send(str.encode(m))

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
