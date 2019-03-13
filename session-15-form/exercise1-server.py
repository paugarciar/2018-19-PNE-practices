import http.server  # libraries to use the server
import socketserver
import termcolor

PORT = 8000


class TestHandler(http.server.BaseHTTPRequestHandler):  # Objects with the properties of the library

    def do_GET(self):

        print("GET received")
        print("Request line:" + self.requestline)
        print(" Cmd: " + self.command)
        print(" Path: " + self.path)
        if self.path == "/":
            page = "introduce_text.html"

        elif self.path == "/introduce_text":
            page = "introduce_text.html"

        else:
            path = self.path
            try:
                path = path.split("=")
                text = path[1]
                print(" User text:", text)
                page = "exercise1-response.html"
            except IndexError:
                page = "error-with-link.html"

        # -- printing the request line
        termcolor.cprint(self.requestline, 'green')

        f = open(page, 'r')
        contents = f.read()
        if page == "exercise1-response.html":
            contents = contents.replace("text", text)

        self.send_response(200)  # everything is OK no matter what have you requested

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
