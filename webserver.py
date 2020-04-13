#!/usr/bin/env python
import SimpleHTTPServer
import SocketServer
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
server = SocketServer.TCPServer(('0.0.0.0', 8080),Handler)
server.serve_forever()
