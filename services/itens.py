# ===================== services/itens.py =====================
from .firebase import pegar_dados  # Importa função para buscar dados do Firebase

# Função que retorna todas as categorias existentes
def pegar_categorias():
    raw = pegar_dados("categories")  # Busca os dados brutos de categorias no Firebase
    out = []
    if isinstance(raw, dict):  # Confirma que os dados retornados são um dicionário
        for uid, nome_categoria in raw.items():  # Itera sobre cada categoria
            if isinstance(nome_categoria, str):  # Garante que o nome é uma string
                out.append({"id": uid, "nome": nome_categoria})  # Adiciona categoria com id e nome
    out.sort(key=lambda c: c["nome"].lower())  # Ordena categorias alfabeticamente
    return out

# Função interna que normaliza os dados de um item, padronizando campos
def _normalizar_item(uid, it):
    nome_item = it.get("nome") or it.get("name") or ""  # Nome do item
    categoria_item = it.get("categoria") or it.get("category") or ""  # Categoria do item
    preco_item = it.get("preco") or it.get("price") or ""  # Preço do item
    imagem_item = it.get("imagem") or it.get("image") or "https://placehold.co/600x400"  # Imagem ou placeholder
    descricao_item = it.get("descricao") or it.get("description") or ""  # Descrição do item
    return {
        "id": uid,
        "nome": nome_item,
        "categoria": categoria_item,
        "preco": preco_item,
        "imagem": imagem_item,
        "descricao": descricao_item
    }

# Retorna lista de itens filtrando por nome e/ou categoria
def pegar_itens_lista(nome=None, categoria=None):
    raw = pegar_dados("items")  # Busca dados brutos de itens no Firebase
    items = []
    if isinstance(raw, dict):
        for uid, it in raw.items():
            item = _normalizar_item(uid, it)  # Normaliza o item
            if nome and nome.lower() not in item["nome"].lower():  # Filtra pelo nome
                continue
            if categoria and categoria != item["categoria"]:  # Filtra pela categoria
                continue
            items.append(item)  # Adiciona item à lista
    items.sort(key=lambda i: (i["categoria"].lower(), i["nome"].lower()))  # Ordena por categoria e nome
    return items

# Retorna todos os itens como um dicionário mapeando id -> dados
def pegar_itens_mapa():
    raw = pegar_dados("items") or {}  # Busca dados brutos
    out = {}
    if isinstance(raw, dict):
        for uid, it in raw.items():
            dados = _normalizar_item(uid, it)  # Normaliza item
            out[uid] = {
                "nome": dados["nome"],
                "categoria": dados["categoria"],
                "preco": dados["preco"],
                "imagem": dados["imagem"],
                "descricao": dados["descricao"]
            }
    return out

# Retorna um item específico pelo ID
def pegar_item(item_id: str):
    raw = pegar_dados(f"items/{item_id}") or {}  # Busca dados do item específico
    if not isinstance(raw, dict):
        return None  # Retorna None se não for um dicionário válido
    return _normalizar_item(item_id, raw)  # Retorna item normalizado
