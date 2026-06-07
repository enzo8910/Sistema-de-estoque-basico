import json
import os

CAMINHO_ARQUIVO= "dados/estoque.json"

def carregar_estoque():
    if not os.path.exists(CAMINHO_ARQUIVO):
        return []

    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar_estoque(estoque):
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(estoque, arquivo, indent=4, ensure_ascii=False)
        