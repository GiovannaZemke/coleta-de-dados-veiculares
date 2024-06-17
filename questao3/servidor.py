from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import csv
import os


class servidor(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        #data receive
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length) 

        #data treatment
        dados = post_data.decode()
        dados = parse_qs(dados, strict_parsing=True)
        dados = {k: v[0] if len(v) == 1 else v for k, v in dados.items()}
        for key, value in dados.items():  
            print(key, value)

        #response for coletor
        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

        #Create txt and csv file
        with open("autoInfoFile.txt", "a") as file:
            file.write("_______________________________\n")
            for key, value in dados.items():  
                file.write('%s:%s\n' % (key, value))

        file_exists = os.path.isfile("autoInfoFile.csv")
        with open("autoInfoFile.csv", "a", newline="") as f:
            fieldnames = dados.keys()
            w = csv.DictWriter(f, fieldnames)
            if not file_exists:
                w.writeheader()
            w.writerow(dados)


#Server Setup
server_address = ('', 8000)
httpd = HTTPServer(server_address, servidor)
print('Iniciando servidor')
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()
print('Desligando servidor')