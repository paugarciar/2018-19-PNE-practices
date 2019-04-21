# Server that process the requests of the client (len, complement, reverse, count, percentage)
# and send an answer for each one

import socket

# SERVER IP, PORT
PORT = 8080
IP = "192.168.1.20"
MAX_OPEN_REQUEST = 5


# Creation of the class Seq
class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        self.strbases = strbases  # self.strbases now represents my initial string

    # Checking if the string entered by the user is a DNA string
    def checking(self):
        if len(self.strbases) == 0:  # first line empty
            result = 'ALIVE'
            return result
        else:
            for letter in self.strbases:
                if (letter != 'A') and (letter != 'C') and (letter != 'T') and (letter != 'G'):
                    result = 'ERROR'  # there are letters that are not bases
                    return result

            result = 'OK'  # all the letters are bases
        return result

    # Length of the string
    def len(self):
        return len(self.strbases)  # returns the length of our string(self.strbases)

    # Complement string
    def complement(self):
        comp_str = ""  # this empty string will receive the complementary bases
        pattern = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        for base in self.strbases:
            comp_str += pattern[base]  # complementary bases are searched in the dictionary
        return comp_str

    # Reverse string
    def reverse(self):
        rev_str = self.strbases[::-1]  # inverting the order of the bases
        return rev_str

    # Number of a concrete base
    def count(self, base):
        result = self.strbases.count(base)  # counting the base that we will introduce
        return result

    # Percentage of a concrete base
    def perc(self, base):
        tl = self.len()
        n = self.count(base)
        percent = round(100.0 * n / tl, 1)  # percentage with one decimal of precision
        return percent

    # Operations related to the options selected
    def match(self, mt):
        send = []  # returns this list
        for element in mt:
            if element == "len":
                s = str(self.len())
            elif element == "complement":
                s = self.complement()
            elif element == "reverse":
                s = self.reverse()
            elif element == "countA" or element == "countC" or element == "countT" or element == "countG":
                base = element[-1]
                s = str(self.count(base))
            elif element == "percA" or element == "percC" or element == "percT" or element == "percG":
                base = element[-1]
                s = str(self.perc(base)) + "%"
            else:
                s = "ERROR"
            send.append(s)

        return send


# Processing the client message
def process_client(cs):

    # creating an empty string to add the response to the commands
    m2_msg = ""

    # reading message from the client
    msg = cs.recv(2048).decode("utf-8")  # maximum length that we want to receive
    m_list = msg.split('\\n')  # divide the message into its different lines

    # The first line is the DNA sequence
    dna = Seq(m_list[0].upper())
    m1 = dna.checking()

    # The rest of the client message are the commands
    m2_list = m_list[1:]

    # Printing in the server the client request
    print("Message from the client: {}".format(msg))
    print("  First line: {}".format(dna))
    print("  Instructions: {}".format(m2_list))

    # Sending the message back to the client (echo server)
    if m1 != "ERROR" and m1 != "ALIVE":
        m2 = dna.match(m2_list)
        # loop to iterate over the elements of the response of the commands
        for element in m2:
            m2_msg += "\n"+element

    cs.send(str.encode(m1+m2_msg))
    cs.close()


# MAIN PROGRAM

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUEST)
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
