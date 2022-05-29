import http.server
import socketserver
HOST="192.168.1.39"
PORT = 8000

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer((HOST, PORT), handler) as httpd:
    print("Serving HTTP on "+str(HOST)+"port "+str(PORT)+"(http://"+str(HOST)+":"+str(PORT)+"/)")
    httpd.serve_forever()