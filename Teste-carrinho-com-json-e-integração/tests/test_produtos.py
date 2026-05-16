import pytest
from unittest.mock import patch, mock_open, MagicMock
from src.produtos import Produtos
import json


MOCK_JSON = json.dumps([
    {"id": 1, "nome": "Monitor", "preco": 1000.0, "quantidade": 5}
])


@patch("builtins.open", new_callable=mock_open, read_data=MOCK_JSON)
def test_buscar_produto(mock_file):
    p = Produtos("qualquer.json")
    prod = p.buscar_por_id(1)
    assert prod["nome"] == "Monitor"


@patch("builtins.open", new_callable=mock_open, read_data=MOCK_JSON)
def test_atualizar_estoque(mock_file):
    p = Produtos("qualquer.json")

    p._salvar = MagicMock()

    p.atualizar_estoque(1, 2)

    prod = p.buscar_por_id(1)
    assert prod["quantidade"] == 3


@patch("builtins.open", new_callable=mock_open, read_data=MOCK_JSON)
def test_estoque_insuficiente(mock_file):
    p = Produtos("qualquer.json")

    with pytest.raises(ValueError):
        p.atualizar_estoque(1, 10)