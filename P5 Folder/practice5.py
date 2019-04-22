# Web server that gives the user access to three different html pages
# It has been programed using HTTP module
import http.server
import socketserver


# Defining the Server's port
PORT = 8001


# Class with our Handler that inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Printing in the server some useful information about the request
        print("GET received")
        print("Request line:"+self.requestline)
        print(" Cmd: "+self.command)
        print(" Path: "+self.path)

        # Accessing to the different html pages
        if self.path == "/":
            page = "index.html"
        elif self.path == "/blue":
            page = "blue.html"
        elif self.path == "/pink":
            page = "pink.html"
        else:
            page = "error.html"
        f = open(page, "r")
        content = f.read()  # reading the contents of the selected page
        f.close()

        # Generating and sending the response message according to the request
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(content)))
        self.end_headers()
        self.wfile.write(str.encode(content))

        return


# MAIN PROGRAM
Handler = TestHandler
socketserver.TCPServer.allow_reuse_address = True  # to avoid problems with the PORT

# main loop that attends the client
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    httpd.serve_forever()
