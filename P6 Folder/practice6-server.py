# Program which send an html page with several options to calculate the characteristics of a DNA string
# The response will be different depending on the instructions and text entered
# sending an error message when it's necessary

import http.server
import socketserver
import termcolor

# Server's port
PORT = 8000


# Creation of seq class with all the definitions related to the string that the user introduces
class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        self.strbases = strbases  # self.strbases now represents my initial string

    # Checking if the string entered by the user is a DNA string
    def checking(self):

        for letter in self.strbases:
            if (letter != 'A') and (letter != 'C') and (letter != 'T') and (letter != 'G') or (len(self.strbases) == 0):
                result = 'ERROR'  # there are letters that are not bases
                return result

        result = self.strbases  # all the letters are bases
        return result

    # Length of the string
    def len(self):
        return len(self.strbases)  # returns the length of our string(self.strbases)

    # Number of a concrete base
    def count(self, base):
        result = self.strbases.count(base)  # counting the base that we will introduce
        return result

    # Percentage of a concrete base
    def perc(self, base):
        tl = self.len()
        n = self.count(base)
        perc = round(100.0 * n / tl, 1)  # percentage with one decimal of precision
        return perc

    # Operations related to the options selected
    def match(self, pth):

        # base for perc and count = path[-1]
        # count/ perc = path[-3]
        element = pth[-3] + pth[-1]

        # In case we had chosen count
        if element == "countA" or element == "countC" or element == "countT" or element == "countG":
            c_msg = "Operation count on the " + pth[-1] + " base: "
            tx1 = "<br>" + c_msg + str(self.strbases.count(pth[-1]))

        # In case we had chosen percentage
        else:
            p_msg = "Operation percentage on the " + pth[-1] + " base: "
            tx1 = "<br>" + p_msg + str(self.perc(pth[-1])) + "%"

        # With checkbutton selected
        if pth[3] == "on":
            l_msg = "The length of your sequence is: "
            tx1 = "<br>" + l_msg + str(self.len()) + tx1

        return tx1


# Class with our Handler that inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):  # Objects with the properties of the library

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Printing in the server some useful information
        print("GET received")
        print("Request line:" + self.requestline)
        print(" Cmd: " + self.command)
        print(" Path: " + self.path)

        # Separating and selecting the information of the path
        calling_response = self.path.split("?")[0]

        # Assigning to the variable page different html pages names in function of the request
        text = ""
        if self.path == "/":
            page = "mainpage.html"

        elif calling_response == "/Seq":  # Using the resource /Seq
            path = self.path
            p = (path.replace("=", ",")).replace("&", ",")
            path = p.split(",")  # Making a list dividing the string in the = and & symbols
            dna = Seq(path[1].upper())  # Replace strbases by the sequence

            if dna.checking() == "ERROR":  # If the DNA sequence is wrong
                text = dna.checking()
            else:
                text = dna.checking() + dna.match(path)  # Otherwise send all the information

            print(" User text:", dna)
            page = "response.html"

        else:
            page = "error.html"

        # -- printing the request line
        termcolor.cprint(self.requestline, 'green')

        f = open(page, 'r')
        contents = f.read()  # reading the contents of the selected page

        # If the html response page is requested change the word text by the text of the user
        if page == "response.html":
            contents = contents.replace("text", text)

        # Generating and sending the response message according to the request
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        # -- sending the body of the response message
        self.wfile.write(str.encode(contents))


# -- MAIN PROGRAM


socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), TestHandler) as httpd:

    # "" means that the program must use the IP address of the computer
    print("Serving at PORT: {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

print("The server is stopped")
