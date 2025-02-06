#!/usr/lib/env python3
# coding : utf-8

import sys
from types import FunctionType
from urllib.parse import urlsplit, unquote
from http.server import HTTPServer, SimpleHTTPRequestHandler

DEFAULT_PORT = 8000
DEFAULT_ADDRESS = "0.0.0.0"


class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        params = dict()
        raddr, rport = self.client_address
        print(f"[+] receive GET request from : {raddr}:{rport}")
        print(f"[+] <- {self.requestline}")
        get_params = urlsplit(self.requestline).query.split(" ")[0]
        
        if get_params:
            for p in get_params.split("&"):
                k, v = p.split("=")
                params[k] = unquote(v)

            try:
                custom_process_params(params)
            except:
                pass
            else:
                print("[+] -> 200")
                self.send_response_only(200)
            finally:
                self.end_headers()
        else:
            # use default behavior like 'python3 -m http.server <port>'
            super().do_GET()


def run(port: int):
    print("[+] Start running Pico HTTP server")
    http_server = HTTPServer((DEFAULT_ADDRESS, port), MyHandler)
    http_server.serve_forever()


def custom_process_params(params: dict):
    # TO DO change for custom process


def main():
    port = None
    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    port = port or DEFAULT_PORT
    run(port)


if __name__ == "__main__":
    main()
