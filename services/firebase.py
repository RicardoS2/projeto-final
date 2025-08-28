# ===================== services/firebase.py =====================

import requests  # Biblioteca para fazer requisições HTTP

# URL base do Firebase Realtime Database
FIREBASE = "https://salete-d88c1-default-rtdb.firebaseio.com".rstrip("/")

# Função interna para gerar a URL completa de um caminho no Firebase
def _url(caminho: str) -> str:
    """
    Recebe um caminho (ex: 'itens/123') e retorna a URL completa para a requisição Firebase.
    """
    return f"{FIREBASE}/{caminho}.json"

# Função interna para fazer requisições HTTP ao Firebase
def _request(metodo: str, caminho: str, dados=None):
    """
    Faz uma requisição HTTP usando requests para o Firebase.
    metodo: 'GET', 'PUT', 'DELETE', etc.
    caminho: caminho relativo no Firebase
    dados: dados enviados para PUT/POST
    Retorna o JSON da resposta ou um dicionário vazio se houver erro.
    """
    try:
        r = requests.request(metodo, _url(caminho), json=dados, timeout=6)
        r.raise_for_status()  # Lança exceção se o status HTTP indicar erro
        return r.json()       # Retorna os dados como dicionário
    except Exception:
        return {}             # Em caso de erro, retorna dicionário vazio

# Função pública para pegar dados de um caminho
def pegar_dados(caminho: str):
    """
    Retorna os dados do caminho especificado no Firebase.
    Se não houver dados, retorna dicionário vazio.
    """
    return _request("GET", caminho) or {}

# Função pública para gravar ou atualizar dados em um caminho
def gravar_dados(caminho: str, dados):
    """
    Grava os dados no caminho especificado do Firebase usando PUT.
    """
    return _request("PUT", caminho, dados)

# Função pública para apagar dados de um caminho
def apagar_dados(caminho: str):
    """
    Remove os dados do caminho especificado no Firebase.
    """
    return _request("DELETE", caminho)
