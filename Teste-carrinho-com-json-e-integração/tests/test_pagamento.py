import pytest
from unittest.mock import patch, MagicMock
from src.pagamento import Pagamento


@patch("src.pagamento.BancoAPI")
def test_pagamento_api(mock_banco_class):
    mock_banco = MagicMock()
    mock_banco.processar.return_value = {"status": "aprovado"}
    mock_banco_class.return_value = mock_banco

    p = Pagamento(mock_banco)

    res = p.pagar(100)

    assert res["status"] == "aprovado"


def test_pix():
    p = Pagamento(MagicMock())
    assert p.calcular_total(100, 1, "pix") == 95


def test_cartao():
    p = Pagamento(MagicMock())
    assert p.calcular_total(100, 1, "cartao") == 105


def test_dinheiro():
    p = Pagamento(MagicMock())
    assert p.calcular_total(100, 1, "dinheiro") == 90


def test_forma_invalida():
    p = Pagamento(MagicMock())
    with pytest.raises(ValueError):
        p.calcular_total(100, 1, "boleto")