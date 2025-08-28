# ===================== services/itens.py =====================
from .firebase import pegar_dados  # Importa função para buscar dados do Firebase

# Função que retorna todas as categorias disponíveis
def pegar_categorias():
    raw = pegar_dados("categories")  # Busca dados brutos de categorias no Firebase
    out = []
    if isinstance(raw, dict):  # Verifica se os dados são um dicionário
        for uid, nome_categoria in raw.items():  # Itera sobre cada categoria
            if isinstance(nome_categoria, str):  # Confirma que o nome da categoria é uma string
                out.append({"id": uid, "nome": nome_categoria})  # Adiciona categoria à lista com id e nome
    out.sort(key=lambda c: c["nome"].lower())  # Ordena categorias alfabeticamente
    return out

# Função interna para padronizar os dados de um item
def _normalizar_item(uid, it):
    nome_item = it.get("nome") or it.get("name") or ""  # Define o nome do item
    categoria_item = it.get("categoria") or it.get("category") or ""  # Define a categoria
    preco_item = it.get("preco") or it.get("price") or ""  # Define o preço
    imagem_item = it.get("imagem") or it.get("image") or "https://placehold.co/600x400"  # Define a imagem ou placeholder
    descricao_item = it.get("descricao") or it.get("description") or ""  # Define a descrição
    return {
        "id": uid,
        "nome": nome_item,
        "categoria": categoria_item,
        "preco": preco_item,
        "imagem": imagem_item,
        "descricao": descricao_item
    }

# Retorna uma lista de itens, podendo filtrar por nome e/ou categoria
def pegar_itens_lista(nome=None, categoria=None):
    raw = pegar_dados("items")  # Busca todos os itens do Firebase
    items = []
    if isinstance(raw, dict):  # Confirma que os dados são válidos
        for uid, it in raw.items():
            item = _normalizar_item(uid, it)  # Normaliza os dados do item
            if nome and nome.lower() not in item["nome"].lower():  # Filtra pelo nome, se informado
                continue
            if categoria and categoria != item["categoria"]:  # Filtra pela categoria, se informada
                continue
            items.append(item)  # Adiciona item à lista
    # Ordena itens primeiro por categoria, depois por nome
    items.sort(key=lambda i: (i["categoria"].lower(), i["nome"].lower()))
    return items

# Retorna todos os itens como um dicionário mapeando ID -> dados
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

# Retorna um item específico pelo seu ID
def pegar_item(item_id: str):
    raw = pegar_dados(f"items/{item_id}") or {}  # Busca dados do item específico
    if not isinstance(raw, dict):  # Retorna None se não for um dicionário válido
        return None
    return _normalizar_item(item_id, raw)  # Retorna item normalizado
