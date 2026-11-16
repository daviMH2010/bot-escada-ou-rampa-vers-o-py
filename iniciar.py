from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import threading
import webbrowser

HOST = "127.0.0.1"
PORT = 8000
ROOT = Path(__file__).resolve().parent

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

if __name__ == "__main__":
    url = f"http://localhost:{PORT}"
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"\nIA de escadas e rampas disponível em: {url}")
    print("Mantenha esta janela aberta. Para encerrar, pressione Ctrl+C.")
    threading.Timer(1, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor encerrado.")
        server.server_close()
