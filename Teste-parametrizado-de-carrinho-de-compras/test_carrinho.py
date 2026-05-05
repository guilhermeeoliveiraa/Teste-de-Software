import pytest
from carrinho import Carrinho


# -------------------------
# TESTES VÁLIDOS (adicionar compra)
# -------------------------
@pytest.mark.parametrize(
    "preco, quantidade, forma, total_esperado",
    [
        (100, 1, "pix", 95.0),
        (200, 2, "cartao", 420.0),
        (50, 5, "dinheiro", 225.0),
        (120, 3, "pix", 342.0),
        (80, 4, "cartao", 336.0),
        (30, 10, "dinheiro", 270.0),
        (500, 1, "pix", 475.0),
        (75, 6, "cartao", 472.5),
        (60, 2, "dinheiro", 108.0),
        (150, 3, "pix", 427.5),
    ]
)
def test_adicionar_compra(preco, quantidade, forma, total_esperado):
    carrinho = Carrinho()
    compra = carrinho.adicionar_compra(preco, quantidade, forma)

    assert compra["total"] == pytest.approx(total_esperado)


# -------------------------
# REGRA: PIX - 5% desconto
# -------------------------
def test_regra_pix():
    carrinho = Carrinho()
    compra = carrinho.adicionar_compra(100, 1, "pix")

    assert compra["desconto"] == 0.05
    assert compra["juros"] == 0


# -------------------------
# REGRA: Cartão - 5% juros
# -------------------------
def test_regra_cartao():
    carrinho = Carrinho()
    compra = carrinho.adicionar_compra(100, 1, "cartao")

    assert compra["juros"] == 0.05
    assert compra["desconto"] == 0


# -------------------------
# REGRA: Dinheiro - 10% desconto
# -------------------------
def test_regra_dinheiro():
    carrinho = Carrinho()
    compra = carrinho.adicionar_compra(100, 1, "dinheiro")

    assert compra["desconto"] == 0.10
    assert compra["juros"] == 0


# -------------------------
# ERRO: preço ou quantidade inválidos
# -------------------------
@pytest.mark.parametrize(
    "preco, quantidade",
    [
        (0, 1),
        (100, 0),
        (-10, 1),
        (100, -5),
    ]
)
def test_valores_invalidos(preco, quantidade):
    carrinho = Carrinho()

    with pytest.raises(ValueError):
        carrinho.adicionar_compra(preco, quantidade, "pix")


# -------------------------
# ERRO: forma de pagamento inválida
# -------------------------
def test_forma_pagamento_invalida():
    carrinho = Carrinho()

    with pytest.raises(ValueError):
        carrinho.adicionar_compra(100, 1, "boleto")


# -------------------------
# TESTE: total geral
# -------------------------
def test_total_geral():
    carrinho = Carrinho()

    carrinho.adicionar_compra(100, 1, "pix")       # 95
    carrinho.adicionar_compra(200, 1, "cartao")    # 210
    carrinho.adicionar_compra(50, 2, "dinheiro")   # 90

    total = carrinho.total_geral()

    assert total == pytest.approx(395.0)


# -------------------------
# TESTE: resumo
# -------------------------
def test_resumo():
    carrinho = Carrinho()

    carrinho.adicionar_compra(100, 1, "pix")       # 95
    carrinho.adicionar_compra(200, 1, "cartao")    # 210

    resumo = carrinho.resumo()

    assert resumo["quantidade_compras"] == 2
    assert resumo["total_geral"] == pytest.approx(305.0)