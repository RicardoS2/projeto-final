# ===================== services/__init__.py =====================

# Importa funções do módulo firebase
# pegar_dados: busca dados do Firebase
# gravar_dados: grava ou atualiza dados no Firebase
# apagar_dados: remove dados do Firebase
from .firebase import pegar_dados, gravar_dados, apagar_dados

# Importa funções do módulo itens
# pegar_categorias: retorna lista de categorias
# pegar_itens_lista: retorna lista de itens filtrada
# pegar_itens_mapa: retorna itens no formato mapa/dicionário
# pegar_item: retorna um item específico pelo ID
from .itens import pegar_categorias, pegar_itens_lista, pegar_itens_mapa, pegar_item

# Define o que será exportado quando alguém fizer:
# from services import *
__all__ = [
    "pegar_dados",        # Função para obter dados do Firebase
    "gravar_dados",       # Função para gravar dados no Firebase
    "apagar_dados",       # Função para apagar dados do Firebase
    "pegar_categorias",   # Função para obter todas as categorias
    "pegar_itens_lista",  # Função para obter lista de itens filtrados
    "pegar_itens_mapa",   # Função para obter itens em formato de mapa
    "pegar_item"          # Função para obter um item específico
]
