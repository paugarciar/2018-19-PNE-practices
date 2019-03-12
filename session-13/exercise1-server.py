import http.server
import socketserver

PORT = 8000


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET received")
        print("Request line:"+self.requestline)
        print(" Cmd: "+self.command)
        print(" Path: "+self.path)

        if self.path == "/":
            page = "index.html"
        elif self.path == "/pink.html":
            page = "pink.html"
        elif self.path == "/blue.html":
            page = "blue.html"
        elif self.path == "/green.html":
            page = "green.html"
        else:
            page = "error.html"

        f = open(page, 'r')
        content = f.read()
        f.close()

        self.send_response(200);
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))
        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    httpd.serve_forever()
