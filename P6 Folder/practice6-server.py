import http.server  # libraries to use the server
import socketserver
import termcolor

PORT = 8000

# Creation of seq class

class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        self.strbases = strbases  # self.strbases now represents my initial string

    def checking(self):
        correct = True

        for letter in self.strbases:
            if (letter != 'A') and (letter != 'C') and (letter != 'T') and (letter != 'G'):
                result = 'ERROR'  # there are letters that are not bases
                correct = False
                return result
        if correct:
            result = self.strbases  # all the letters are bases
            return result

    def len(self):
        return len(self.strbases)  # returns the length of our string(self.strbases)

    def complement(self):
        comp_str = ""  # this empty string will receive the complementary bases
        pattern = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        for base in self.strbases:
            comp_str += pattern[base]  # complementary bases are searched in the dictionary
        return comp_str

    def reverse(self):
        rev_str = self.strbases[::-1]  # inverting the order of the bases
        return rev_str

    def count(self, base):
        result = self.strbases.count(base)  # counting the base that we will introduce
        return result

    def perc(self, base):
        tl = len(self.strbases)
        n = self.strbases.count(base)
        if tl > 0:
            perc = round(100.0 * n / tl, 1)  # percentage with one decimal of precision

        else:
            perc = 0  # if there is an empty string
        return perc


class TestHandler(http.server.BaseHTTPRequestHandler):  # Objects with the properties of the library

    def do_GET(self):

        print("GET received")
        print("Request line:" + self.requestline)
        print(" Cmd: " + self.command)
        print(" Path: " + self.path)
        if self.path == "/":
            page = "mainpage.html"

        else:
            path = self.path
            try:
                path = path.split("=")
                if len(path) == 4:  # Checkbutton deselected
                    text = Seq(path[1])

                else:  # When the checkbutton is selected, the length is 5
                    for elements in path:
                        elements.split("&")
                    tx = path[1]  # Text user
                    tx2 = path[3]  # check selected
                    tx3 = path[5]  # perc or count option
                    tx4 = path[7]  # base selected
                    text = Seq(tx[0])  # Replace strbases by the sequence
                print(" User text:", text)
                page = "response.html"
            except IndexError:
                page = "error-with-link.html"

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
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    # "" means that the program must use the IP address of the computer
    print("Serving at PORT: {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

print("The server is stopped")

# IMPLEMENT CLASSES AND ASK ABOUT THE RESOURCE /SEQ, CREATE ALSO ERROR PAGE
