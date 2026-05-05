import pytest
from src.pagamento import Pagamento


class FakeBanco:
    def processar(self, valor):
        return {"status": "aprovado"}


def test_pix():
    p = Pagamento(FakeBanco())
    assert p.calcular_total(100, 1, "pix") == 95


def test_cartao():
    p = Pagamento(FakeBanco())
    assert p.calcular_total(100, 1, "cartao") == 105


def test_dinheiro():
    p = Pagamento(FakeBanco())
    assert p.calcular_total(100, 1, "dinheiro") == 90


def test_pagamento_api():
    p = Pagamento(FakeBanco())
    res = p.pagar(100)
    assert res["status"] == "aprovado"