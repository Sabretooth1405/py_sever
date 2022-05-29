
import http.server
import os
HOST="192.168.1.39"

class RequestHandler(http.server.BaseHTTPRequestHandler):
    '''Handle HTTP requests by returning a fixed 'page'.'''

    def do_GET(self):
         
        try:
            print   ('Get request received')
            # Figure out what exactly is being requested.
           # if '-' in self.path:
                #path_parse(self.path)
            
            full_path = os.getcwd() + self.path
            print(self.path)
            # It doesn't exist...
            if not os.path.exists(full_path):
                self.handle_file(os.getcwd()+"/index.html")
                print("error path doesn't exist")
            # ...it's a file...
            elif os.path.isfile(full_path):
                self.handle_file(full_path)

            # ...it's something we don't handle.
            else:
                   self.handle_file(os.getcwd()+"/index.html")
                   print("error unknown object")
    


        # Handle errors.
        except Exception as msg:
            self.handle_error(msg)
    def do_ROUT(self):
        full_path = os.getcwd() + self.path
        print(full_path)

    def handle_file(self, full_path):
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
            self.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(self.path, msg)
            self.handle_error(msg)
    Error_Page = """\
        <html>
        <body>
        <h1>Error accessing {path}</h1>
        <p>{msg}</p>
        </body>
        </html>
        """
   
    
    # Handle unknown objects.

    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content, 404)

    # Send actual content.
    def send_content(self, content, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)
    

if __name__ == '__main__':
    serverAddress = (HOST, 8000)
    server = http.server.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
