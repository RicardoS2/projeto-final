# services/firebase.py
import requests

FIREBASE = "https://salete-d88c1-default-rtdb.firebaseio.com".rstrip("/")

def _url(caminho: str) -> str:
    return f"{FIREBASE}/{caminho}.json"

def _request(metodo: str, caminho: str, dados=None):
    try:
        r = requests.request(metodo, _url(caminho), json=dados, timeout=6)
        r.raise_for_status()
        return r.json()
    except Exception:
        return {}

def pegar_dados(caminho: str):
    return _request("GET", caminho) or {}

def gravar_dados(caminho: str, dados):
    return _request("PUT", caminho, dados)

def apagar_dados(caminho: str):
    return _request("DELETE", caminho)
