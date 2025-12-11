#!/usr/bin/env python3
"""
Very simple HTTP server in python.

Usage::
    ./dummy-web-server.py [<port>]

Send a GET request::
    curl http://localhost

Send a HEAD request::
    curl -I http://localhost

Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost

"""
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import datetime

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        with open("IsProvisioning.log", "a") as f:
            f.write(str(datetime.datetime.now()) + " " + self.command + " " + self.path + "\n")
        self._set_headers()
        self.wfile.write(b"<html><body><h1>200 OK</h1>Service ready.</body></html>")

    def do_HEAD(self):
        with open("IsProvisioning.log", "a") as f:
            f.write(str(datetime.datetime.now()) + " " + self.command + " " + self.path + "\n")
        self._set_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # Gets the size of data
        post_data = self.rfile.read(content_length)  # Gets the data itself
        with open("IsProvisioning.log", "a") as f:
            f.write(str(datetime.datetime.now()) + " " + self.command + " " + self.path + "\n")
            f.write(post_data.decode() + "\n")  # Print post data
        self._set_headers()
        self.wfile.write(b"<html><body><h1>200 OK</h1>Service ready.</body></html>")

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    # Get port from environment variable
    port = os.environ.get("PORT", 80)
    run(port=int(port))
