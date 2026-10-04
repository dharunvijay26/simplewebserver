from http.server import HTTPServer, BaseHTTPRequestHandler

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = """
        <html>
        <head>
            <title>Simple Webserver</title>
        </head>
        <body>
            <h1>Simple Webserver</h1>

            <h2>Name: Dharun Vijay</h2>
            <h2>Register Number: 26019647</h2>

            <h3>TCP/IP Protocol Suite</h3>
            <p>HTTP</p>
            <p>TCP</p>
            <p>IP</p>
            <p>DNS</p>
        </body>
        </html>
        """

        self.wfile.write(bytes(html, "utf-8"))


server = HTTPServer(("127.0.0.1", 8000), MyServer)

print("Server started at http://127.0.0.1:8000")

server.serve_forever()