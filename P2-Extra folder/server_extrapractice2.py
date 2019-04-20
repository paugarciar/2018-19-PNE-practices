# server that reads the sequence string and creates a Seq object. Then returns the complement sequence to the client
import socket

# Configure the Server's IP and PORT
PORT = 8081
IP = "172.20.10.6"
MAX_OPEN_REQUESTS = 5

# Counting the number of connections
number_con = 0

# Creating an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Creating the Seq class
class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        self.strbases = strbases

    def complement(self):
        comp_str = ""  # this empty string will receive the complementary bases
        pattern = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        for base in self.strbases:
            comp_str += pattern[base]  # complementary bases are searched in the dictionary
        return comp_str


try:
    serversocket.bind((IP, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        # Another connection!e
        number_con += 1

        # Print the connection number
        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        # Read the message from the client, if any
        msg = clientsocket.recv(2048).decode("utf-8").upper()
        sequence = Seq(msg).complement()
        print("Message from client: {}".format(msg))
        print("Complement sequence: {}\n".format(sequence))
        # Send the complement sequence
        message = " The complement sequence is:"+sequence+"\n"
        send_bytes = str.encode(message)
        # We must write bytes, not a string
        clientsocket.send(send_bytes)
        clientsocket.close()

# Dealing with errors
except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()
