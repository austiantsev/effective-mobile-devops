from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello from Effective Mobile!')

server = HTTPServer(('0.0.0.0', 8080), Handler)
print('Server started on port 8080')
server.serve_forever()
