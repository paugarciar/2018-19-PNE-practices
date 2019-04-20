# Client that uses objects to transform a sequence entered by the user into
# a complement-reverse sequence

import socket


# Definition of the class
class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        self.strbases = strbases  # self.strbases now represents my initial string

    def complement(self):
        comp_str = ""  # this empty string will receive the complementary bases
        pattern = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        for base in self.strbases:
            comp_str += pattern[base]  # complementary bases are searched in the dictionary
        return comp_str

    def reverse(self):
        rev_str = self.strbases[::-1]  # inverting the order of the bases
        return rev_str


# main program

# loop to go on chatting
connected = True
while connected:
    # socket for communicating with the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("socket created")

    PORT = 8081
    IP = "192.168.1.20"

    s.connect((IP, PORT))
    seq1 = Seq(input("\nwrite a sequence to obtain the reverse-complement: ").upper())
    seq2 = Seq(seq1.reverse()).complement()
    print("reverse-complement sequence: ", seq2)
    # converting the strings into binary code
    s.send(str.encode(seq2))

    s.close()
    print("--sequence sent to the server--")
