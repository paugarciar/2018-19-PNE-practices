import http.server  # libraries to use the server
import socketserver
import termcolor

PORT = 8001


# Creation of seq class


class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        self.strbases = strbases  # self.strbases now represents my initial string

    def checking(self):
        correct = True

        for letter in self.strbases:
            if (letter != 'A') and (letter != 'C') and (letter != 'T') and (letter != 'G') or (len(self.strbases) == 0):
                result = 'ERROR'  # there are letters that are not bases
                correct = False
                return result
        if correct:
            result = self.strbases  # all the letters are bases
            return result

    def len(self):
        return len(self.strbases)  # returns the length of our string(self.strbases)

    def count(self, base):
        result = self.strbases.count(base)  # counting the base that we will introduce
        return result

    def perc(self, base):
        tl = self.len()
        n = self.count(base)
        perc = round(100.0 * n / tl, 1)  # percentage with one decimal of precision
        return perc

    def match(self, pth):
        # base for perc and count = path[-1]
        # count/ perc = path[-2]


        element = pth[-3] + pth[-1]
        if element == "countA" or element == "countC" or element == "countT" or element == "countG":
            c_msg = "Operation count on the " + pth[-1] + " base: "
            tx1 = "<br>" + c_msg + str(self.strbases.count(pth[-1]))

        else:
            p_msg = "Operation percentage on the " + pth[-1] + " base: "
            tx1 = "<br>" + p_msg + str(self.perc(pth[-1])) + "%"

        # checkbutton selected
        if pth[3] == "on":
            l_msg = "The length of your sequence is: "
            tx1 = "<br>" + l_msg + str(self.len()) + tx1

        return tx1

class TestHandler(http.server.BaseHTTPRequestHandler):  # Objects with the properties of the library

    def do_GET(self):

        print("GET received")
        print("Request line:" + self.requestline)
        print(" Cmd: " + self.command)
        print(" Path: " + self.path)
        calling_response = self.path.split("?")[0]
        if self.path == "/":
            page = "mainpage.html"

        elif calling_response == "/Seq":
            path = self.path
            p = (path.replace("=", ",")).replace("&", ",")
            path = p.split(",")  # Making a list dividing the string in the = and & symbols
            dna = Seq(path[1].upper())  # Replace strbases by the sequence

            if dna.checking() == "ERROR":
                text = dna.checking()
            else:
                text = dna.checking() + dna.match(path)


            print(" User text:", dna)
            page = "response.html"

        else:
            page ="error.html"

        # -- printing the request line
        termcolor.cprint(self.requestline, 'green')

        f = open(page, 'r')
        contents = f.read()

        # If the html response page is requested change the word text by the text of the user
        if page == "response.html":
            contents = contents.replace("text", text)

        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        # -- sending the body of the response message
        self.wfile.write(str.encode(contents))

# -- Main program

socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), TestHandler) as httpd:

    # "" means that the program must use the IP address of the computer
    print("Serving at PORT: {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

print("The server is stopped")
