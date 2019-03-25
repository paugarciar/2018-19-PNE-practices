import socket

PORT = 8081
IP = "192.168.1.106"
MAX_OPEN_REQUEST = 5


# Analysis of the first line of the message
def first_line(fl):
    correct = True
    if len(fl) == 0:  # first line empty
        result = 'ALIVE'
        return result
    else:
        for letter in fl:
            if (letter != 'A') and (letter != 'C') and (letter != 'T') and (letter != 'G'):
                result = 'ERROR'  # there are letters that are not bases
                correct = False
                return result
        if correct:
            result = 'OK'  # all the letters are bases
            return result


# Length function
def length(l):
    leng = len(l)
    return leng


# Complement function
def complement(cpl):
    comp_str = ""  # this empty string will receive the complementary bases
    pattern = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    for base in cpl:
        comp_str += pattern[base]  # complementary bases are searched in the dictionary
    return comp_str


# Reverse function
def reverse(rv):
    rev_str = rv[::-1]  # inverting the order of the bases
    return rev_str


# Count function
def count(ct, bs):
    cnt = ct.count(bs)  # counting the base that we will introduce
    return cnt


# Percentage function
def perc(pc, bs):
    tl = length(pc)
    n = pc.count(bs)
    percent = round(100.0 * n / tl, 1)  # percentage with one decimal of precision
    return percent


# Function that look for information requested
def match(mt, seq):
    send = []  # returns this list
    for element in mt:
        if element == "len":
            s = str(length(seq))
        elif element == "complement":
            s = complement(seq)
        elif element == "reverse":
            s = reverse(seq)
        elif element == "countA" or element == "countC" or element == "countT" or element == "countG":
            base = element[-1]
            s = str(count(seq, base))
        elif element == "percA" or element == "percC" or element == "percT" or element == "percG":
            base = element[-1]
            s = str(perc(seq, base))+"%"
        else:
            s = "ERROR"
        send.append(s)

    return send


def process_client(cs):
    m2_msg = ""
    # reading message from the client
    msg = cs.recv(2048).decode("utf-8")  # maximum length that we want to receive
    m_list = msg.split('\\n')  # divide the message into its different lines
    dna = m_list[0].upper()
    m1 = first_line(dna)
    m2_list = m_list[1:]
    print("Message from the client: {}".format(msg))
    print("  First line: {}".format(dna))
    print("  Instructions: {}".format(m2_list))

    # sending the message back to the client (echo server)
    if m1 != "ERROR" and m1 != "ALIVE":
        m2 = match(m2_list, dna)
        # loop to iterate over the elements of the result
        for element in m2:
            m2_msg += "\n"+element
    else:
        m2_msg = ""
    cs.send(str.encode(m1+m2_msg))
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
