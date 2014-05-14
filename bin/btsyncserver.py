#!/usr/bin/env python
import ssl
import socket
import sys
from SocketServer import TCPServer, BaseRequestHandler, BaseServer

from btsync import BTSync

class BTSyncHandler(BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        char = self.request.recv(1024)
        if len(char) == 1:
            len_secret = ord( char )
            self.request.send('a')
            secret = ''
            while len(secret) < len_secret:
              chunk = self.request.recv( len_secret - len(secret) )
              secret = secret + chunk
            b = BTSync()
            r = b.register_secret( secret )
            self.request.sendall( str(r) )
        self.request.shutdown(2)
        self.request.close()

class STCPServer(TCPServer):
    def __init__(self, server_address, RequestHandlerClass, certfile, bind_and_activate=True):
        # See SocketServer.TCPServer.__init__
        # (added ssl-support):
        BaseServer.__init__(self, server_address,RequestHandlerClass)
        self.socket = ssl.wrap_socket(socket.socket(self.address_family,self.socket_type),server_side=True,certfile=certfile)

        if bind_and_activate:
            self.server_bind()
            self.server_activate()

if __name__ == '__main__':
    listen = ('localhost',10023)
    certfile = 'cert.pem'
    server = TCPServer(listen, BTSyncHandler, certfile)
    try:
        print 'server start'
        server.serve_forever()
    except KeyboardInterrupt, err:
        print 'server shutdown\n'
        server.shutdown()
