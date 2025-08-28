# app.py
from flask import Flask, render_template, request, redirect, url_for
import uuid, os

from services import pegar_itens_lista, pegar_itens_mapa, pegar_item, pegar_categorias
from services.firebase import gravar_dados, apagar_dados, pegar_dados
from utils import salvar_imagem

app = Flask(__name__)

# Config simples de uploads (a pasta é criada no utils.salvar_imagem também)
PORTA = int(os.environ.get("PORT", 5000))

@app.route("/")
def index():
    filtro_nome = request.args.get("nome", "").strip()
    filtro_categoria = request.args.get("categoria", "").strip()
    itens = pegar_itens_lista(nome=filtro_nome, categoria=filtro_categoria)
    categorias = [c["nome"] for c in pegar_categorias()]
    return render_template("index.html", items=itens, categories=categorias,
                           filtro_nome=filtro_nome, filtro_categoria=filtro_categoria)

@app.route("/item/<item_id>")
def item_page(item_id):
    item = pegar_item(item_id)
    if not item:
        return "Item não encontrado", 404
    categorias = [c["nome"] for c in pegar_categorias()]
    return render_template("item.html", item=item, categories=categorias)

@app.route("/admin")
def admin():
    itens_mapa = pegar_itens_mapa()
    categorias = pegar_categorias()
    return render_template("admin.html", items=itens_mapa, categories=categorias, edit_item=None)

@app.route("/admin/editar/<item_id>")
def admin_editar(item_id):
    itens_mapa = pegar_itens_mapa()
    categorias = pegar_categorias()
    item_editar = pegar_item(item_id)
    if not item_editar:
        return redirect(url_for("admin"))
    return render_template("admin.html", items=itens_mapa, categories=categorias, edit_item=item_editar)

@app.route("/admin/salvar", methods=["POST"])
@app.route("/admin/salvar/<item_id>", methods=["POST"])
def admin_salvar(item_id=None):
    nome = request.form.get("nome", "").strip()
    categoria = request.form.get("categoria", "").strip()
    preco = request.form.get("preco", "").strip()
    descricao = request.form.get("descricao", "").strip()
    imagem_url = request.form.get("imagem", "").strip()
    arquivo_imagem = request.files.get("arquivo_imagem")

    if not nome or not categoria:
        return redirect(url_for("admin"))

    if arquivo_imagem and arquivo_imagem.filename:
        url_salva = salvar_imagem(arquivo_imagem)
        if url_salva:
            imagem_url = url_salva

    if not imagem_url:
        imagem_url = f"https://placehold.co/600x400?text={nome.replace(' ', '+')}"

    dados = {
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "imagem": imagem_url,
        "descricao": descricao
    }

    uid = item_id if item_id else uuid.uuid4().hex[:12]
    gravar_dados(f"items/{uid}", dados)
    return redirect(url_for("admin"))

@app.route("/admin/excluir/<item_id>")
def admin_excluir(item_id):
    apagar_dados(f"items/{item_id}")
    return redirect(url_for("admin"))

@app.route("/admin/adicionar_categoria", methods=["POST"])
def admin_adicionar_categoria():
    novo_nome = request.form.get("categoria", "").strip()
    if not novo_nome:
        return redirect(url_for("admin"))
    mapa_cats = pegar_dados("categories") or {}
    if novo_nome in mapa_cats.values():
        return redirect(url_for("admin"))
    novo_id = f"c_{uuid.uuid4().hex[:10]}"
    gravar_dados(f"categories/{novo_id}", novo_nome)
    return redirect(url_for("admin"))

@app.route("/admin/excluir_categoria/<cat_id>")
def admin_excluir_categoria(cat_id):
    apagar_dados(f"categories/{cat_id}")
    return redirect(url_for("admin"))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=PORTA, debug=True)
