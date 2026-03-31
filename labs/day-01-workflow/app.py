import http.server 
import socketserver

PORT = 9000
Handler = http.server.SimpleHTTPRequestHandler

print(f"Servidor MLOps arrancando en el puerto {PORT}...")
with socketserver.TCPServer(("",PORT), Handler) as httpd:
    httpd.serve_forever()

