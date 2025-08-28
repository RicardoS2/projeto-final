# utils/upload.py
import os, uuid
from werkzeug.utils import secure_filename
from flask import url_for

PASTA_UPLOADS = "static/uploads"
EXTENSOES_PERMITIDAS = {"png", "jpg", "jpeg", "gif"}

def extensao_permitida(filename: str) -> bool:
    return bool(filename) and "." in filename and filename.rsplit(".", 1)[1].lower() in EXTENSOES_PERMITIDAS

def salvar_imagem(arquivo):
    if arquivo and arquivo.filename and extensao_permitida(arquivo.filename):
        os.makedirs(PASTA_UPLOADS, exist_ok=True)
        nome_seguro = secure_filename(arquivo.filename)
        nome_armazenado = f"{uuid.uuid4().hex}_{nome_seguro}"
        caminho = os.path.join(PASTA_UPLOADS, nome_armazenado)
        arquivo.save(caminho)
        return url_for("static", filename=f"uploads/{nome_armazenado}")
    return None
