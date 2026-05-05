import pytest
import json
import os

from src.produtos import Produtos
from src.pagamento import Pagamento
from src.venda import processar_venda


@pytest.fixture
def ambiente():
    arquivo = "temp.json"
    dados = [
        {"id": 101, "nome": "Teclado Mecânico", "preco": 250.0, "quantidade": 8},
        {"id": 103, "nome": "SSD", "preco": 0.0, "quantidade": 10},
        {"id": 105, "nome": "Cadeira", "preco": -800.0, "quantidade": 3},
        {"id": 106, "nome": "Headset", "preco": 350.0, "quantidade": 0}
    ]

    with open(arquivo, "w") as f:
        json.dump(dados, f)

    produtos = Produtos(arquivo)
    pagamento = Pagamento(banco_api=None)

    yield produtos, pagamento

    if os.path.exists(arquivo):
        os.remove(arquivo)


# -------------------------
# CASO VÁLIDO
# -------------------------
def test_venda_produto_valido(ambiente):
    produtos, pagamento = ambiente

    class MockBanco:
        def processar(self, valor):
            return {"status": "aprovado"}

    pagamento.banco = MockBanco()

    resultado = processar_venda(produtos, pagamento, 101, 2, "pix")

    assert resultado["status"] == "aprovado"


# -------------------------
# PREÇO ZERO
# -------------------------
def test_preco_zero(ambiente):
    produtos, pagamento = ambiente

    class MockBanco:
        def processar(self, valor):
            return {"status": "aprovado"}

    pagamento.banco = MockBanco()

    with pytest.raises(ValueError):
        processar_venda(produtos, pagamento, 103, 1, "pix")


# -------------------------
# PREÇO NEGATIVO
# -------------------------
def test_preco_negativo(ambiente):
    produtos, pagamento = ambiente

    class MockBanco:
        def processar(self, valor):
            return {"status": "aprovado"}

    pagamento.banco = MockBanco()

    with pytest.raises(ValueError):
        processar_venda(produtos, pagamento, 105, 1, "pix")


# -------------------------
# ESTOQUE ZERO
# -------------------------
def test_estoque_zero(ambiente):
    produtos, pagamento = ambiente

    class MockBanco:
        def processar(self, valor):
            return {"status": "aprovado"}

    pagamento.banco = MockBanco()

    with pytest.raises(ValueError):
        processar_venda(produtos, pagamento, 106, 1, "pix")