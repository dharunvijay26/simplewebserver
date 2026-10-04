# EX01 Developing a Simple Webserver
## Date:

## AIM:
To develop a simple webserver to serve html pages and display the Windows Specifications of your Laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
'''
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

'''
## OUTPUT:
![alt text](<Screenshot 2026-10-04 112749.png>)
![alt text](<Screenshot 2026-10-04 113112.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
