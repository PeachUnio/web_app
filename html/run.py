from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHandler(BaseHTTPRequestHandler):
    """Класс для открытия сервера"""

    def do_GET(self):
        with open('contacts.html', 'r', encoding='utf-8') as file:
            html_content = file.read()

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))


def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHandler)
    print('Сервер запущен на http://localhost:8000')
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()