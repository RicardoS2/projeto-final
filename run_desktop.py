# run_desktop.py
import threading
import time
import webbrowser
import requests
from app import app

# tenta importar pywebview; se não estiver disponível, usar navegador
try:
    import webview
    HAS_WEBVIEW = True
except ImportError:
    HAS_WEBVIEW = False

HOST = "127.0.0.1"
PORT = 5050
URL = f"http://{HOST}:{PORT}"

def start_flask():
    # inicia Flask sem reloader
    app.run(host=HOST, port=PORT, debug=False, use_reloader=False)

def wait_server(url, timeout=10):
    """Espera o servidor estar pronto"""
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            r = requests.get(url, timeout=1)
            if r.status_code < 500:
                return True
        except Exception:
            pass
        time.sleep(0.2)
    return False

if __name__ == "__main__":
    # inicia Flask em thread separada
    threading.Thread(target=start_flask, daemon=True).start()

    # espera servidor ficar disponível
    if not wait_server(URL, timeout=10):
        print(f"Servidor não iniciou no tempo esperado. Abra manualmente em {URL}")
        webbrowser.open(URL)
    else:
        if HAS_WEBVIEW:
            # cria janela nativa com webview
            webview.create_window("Catálogo Salete", URL, width=1000, height=800)
            webview.start()
        else:
            # fallback: abre no navegador padrão
            webbrowser.open(URL)
            print("pywebview não instalado — abrindo no navegador padrão.")
