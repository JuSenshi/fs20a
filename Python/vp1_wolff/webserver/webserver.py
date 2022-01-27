from http.server import BaseHTTPRequestHandler, HTTPServer
import pathlib
import time

hostName = "localhost"
serverPort = 8080

datei = "<html><head><title>kacke</title></head><body>wasn bullshit</body></html>"

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        p = pathlib.Path().resolve()
        print(p)
        f = open(str(p) + self.path, 'r').read()
        print(f)
        self.wfile.write(bytes(f, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")