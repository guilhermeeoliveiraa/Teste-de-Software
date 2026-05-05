import pytest
from src.produtos import Produtos
import json
import os


@pytest.fixture
def db_temp():
    arquivo = "temp.json"
    dados = [{"id": 1, "nome": "Monitor", "preco": 1000.0, "quantidade": 5}]

    with open(arquivo, "w") as f:
        json.dump(dados, f)

    yield Produtos(arquivo)

    os.remove(arquivo)


def test_buscar_produto(db_temp):
    p = db_temp.buscar_por_id(1)
    assert p["nome"] == "Monitor"


def test_atualizar_estoque(db_temp):
    db_temp.atualizar_estoque(1, 2)
    p = db_temp.buscar_por_id(1)
    assert p["quantidade"] == 3


def test_estoque_insuficiente(db_temp):
    with pytest.raises(ValueError):
        db_temp.atualizar_estoque(1, 10)