#!/usr/bin/python
# coding: utf-8

import json
import time
from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler
import users

class EndPoint (BaseHTTPRequestHandler) :

    def do_GET(self):
        
        if self.path == "/" :
            #enviar o código de resposta:
            self.send_response(200)
            #enviar uma linha em branco para terminar o cabeçalho:
            self.wfile.write("\n")
            #enviar resposta:
            json.dump(users.info(), self.wfile, indent=4, sort_keys=True)

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), EndPoint)
    print time.asctime(), "Server Starts, use <Ctrl-C> to stop"        
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
