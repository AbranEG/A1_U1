from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse


class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

def do_GET(self):
    if self.path == "/":
        
        with open("home.html", "r") as file:
            content = file.read()

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode("utf-8"))
    else:
        self.send_response(404)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write("<h1>ERROR 404:Not Found</h1>".encode("utf-8"))


def get_response(self, host, user_agent):
   
    query_data = self.query_data()
    autor = query_data.get('autor', 'desconocido')


    return f"""
    <h1>Proyecto: {self.url().path} Autor: {autor}</h1>
    <p> Host: {host} </p>
    <p> User-Agent: {user_agent} </p>
    """



if __name__ == "__main__":
    print("Starting server on port 8000")
    server = HTTPServer(("localhost", 8000), WebRequestHandler) #SE CAMBIO AL PUERTO 8000 
    server.serve_forever()

