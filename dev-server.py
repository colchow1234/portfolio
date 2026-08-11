#!/usr/bin/env python3
"""Local preview server that mimics the pretty-URL rewrites from vercel.json
(/home -> index.html, /credits -> credits.html), so nav links work the same
way locally as they do on the live site."""
import http.server
import socketserver
import sys

PORT = 8000

REWRITES = {
    '/home': '/index.html',
    '/credits': '/credits.html',
    '/sketchbook': '/sketchbook.html',
}

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in REWRITES:
            self.path = REWRITES[self.path]
        return super().do_GET()

    def log_message(self, format, *args):
        pass  # keep the terminal quiet

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            sys.exit(0)
