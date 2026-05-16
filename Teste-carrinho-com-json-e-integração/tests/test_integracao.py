import pytest
import json
import os
from unittest.mock import patch, MagicMock

from src.produtos import Produtos
from src.venda import processar_venda


@pytest.fixture
def banco_temporario():
    arquivo = "temp_db.json"
    dados_iniciais = [
        {"id": 101, "nome": "Teclado Mecânico", "preco": 250.0, "quantidade": 8}
    ]

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados_iniciais, f)

    repo = Produtos(arquivo)
    yield repo

    if os.path.exists(arquivo):
        os.remove(arquivo)


@pytest.fixture
def banco_com_dados_invalidos():
    arquivo = "invalid_db.json"
    dados = [
        {"id": 999, "nome": "Produto de Graça", "preco": 0.0, "quantidade": 10},
        {"id": 888, "nome": "Produto Negativo", "preco": -50.0, "quantidade": 5},
        {"id": None, "nome": "Produto Sem ID", "preco": 10.0, "quantidade": 1}
    ]

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f)

    repo = Produtos(arquivo)
    yield repo

    if os.path.exists(arquivo):
        os.remove(arquivo)


@patch("src.pagamento.Pagamento")
def test_venda_integrada(mock_pagamento_class, banco_temporario):
    mock_pagamento = MagicMock()
    mock_pagamento.calcular_total.return_value = 475.0
    mock_pagamento.pagar.return_value = {"status": "aprovado"}

    mock_pagamento_class.return_value = mock_pagamento

    resultado = processar_venda(
        banco_temporario,
        mock_pagamento,
        101,
        2,
        "pix"
    )

    assert resultado["produto"] == "Teclado Mecânico"
    assert resultado["status"] == "aprovado"


@patch("src.pagamento.Pagamento")
def test_venda_id_inexistente(mock_pagamento_class, banco_com_dados_invalidos):
    mock_pagamento = MagicMock()
    mock_pagamento_class.return_value = mock_pagamento

    with pytest.raises(ValueError, match="Produto não encontrado"):
        processar_venda(banco_com_dados_invalidos, mock_pagamento, 777, 1, "pix")