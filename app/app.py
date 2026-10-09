
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            response = {
                "status": "healthy",
                "service": "platform-demo"
            }
            self.send_response(200)
        elif self.path == "/":
            response = {
                "message": "Hello from the platform demo",
                "service": "platform-demo"
            }
            self.send_response(200)
        else:
            response = {"error": "Not found"}
            self.send_response(404)

        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))

    def log_message(self, format, *args):
        print(f"{self.address_string()} - {format % args}")


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), HealthHandler)
    print("Platform demo listening on port 8080")
    server.serve_forever()
