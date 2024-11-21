from http.server import HTTPServer, BaseHTTPRequestHandler
import json

HOST = '127.0.0.1'
PORT = 8000

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(b'<body><button>GET REQUEST</button></body>')

    def do_POST(self):
        content_lenght = int(self.headers['Content-Length'])

        post_data = self.rfile.read(content_lenght)

        print(f'RECIVED POST DATA{post_data.decode('utf-8')}')

        response_data = {
            'message' : 'data recived successfully',
            'data': post_data.decode('utf-8')}

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        self.wfile.write(json.dumps(response_data).encode('utf-8'))


server = HTTPServer((HOST, PORT), RequestHandler)
print(f'Server is running at {HOST}:{PORT}')
server.serve_forever()