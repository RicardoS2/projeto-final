# services/itens.py
from .firebase import pegar_dados

def pegar_categorias():
    raw = pegar_dados("categories")
    out = []
    if isinstance(raw, dict):
        for uid, nome_categoria in raw.items():
            if isinstance(nome_categoria, str):
                out.append({"id": uid, "nome": nome_categoria})
    out.sort(key=lambda c: c["nome"].lower())
    return out

def _normalizar_item(uid, it):
    nome_item = it.get("nome") or it.get("name") or ""
    categoria_item = it.get("categoria") or it.get("category") or ""
    preco_item = it.get("preco") or it.get("price") or ""
    imagem_item = it.get("imagem") or it.get("image") or "https://placehold.co/600x400"
    descricao_item = it.get("descricao") or it.get("description") or ""
    return {
        "id": uid,
        "nome": nome_item,
        "categoria": categoria_item,
        "preco": preco_item,
        "imagem": imagem_item,
        "descricao": descricao_item
    }

def pegar_itens_lista(nome=None, categoria=None):
    raw = pegar_dados("items")
    items = []
    if isinstance(raw, dict):
        for uid, it in raw.items():
            item = _normalizar_item(uid, it)
            if nome and nome.lower() not in item["nome"].lower():
                continue
            if categoria and categoria != item["categoria"]:
                continue
            items.append(item)
    items.sort(key=lambda i: (i["categoria"].lower(), i["nome"].lower()))
    return items

def pegar_itens_mapa():
    raw = pegar_dados("items") or {}
    out = {}
    if isinstance(raw, dict):
        for uid, it in raw.items():
            dados = _normalizar_item(uid, it)
            out[uid] = {
                "nome": dados["nome"],
                "categoria": dados["categoria"],
                "preco": dados["preco"],
                "imagem": dados["imagem"],
                "descricao": dados["descricao"]
            }
    return out

def pegar_item(item_id: str):
    raw = pegar_dados(f"items/{item_id}") or {}
    if not isinstance(raw, dict):
        return None
    return _normalizar_item(item_id, raw)
