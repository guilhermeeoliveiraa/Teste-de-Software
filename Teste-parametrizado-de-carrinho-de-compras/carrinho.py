class Carrinho:
    def __init__(self):
        self.compras = []

    def adicionar_compra(self, preco, quantidade, forma_pagamento):
        forma = forma_pagamento.lower()

        if preco <= 0 or quantidade <= 0:
            raise ValueError("Preço e quantidade devem ser maiores que zero")

        if forma not in ["pix", "cartao", "dinheiro"]:
            raise ValueError("Forma de pagamento inválida")

        desconto = 0
        juros = 0

        # Regras
        if forma == "pix":
            desconto = 0.05
        elif forma == "cartao":
            juros = 0.05
        elif forma == "dinheiro":
            desconto = 0.10

        # Regra: não pode ter os dois
        if desconto > 0 and juros > 0:
            raise ValueError("Não pode ter juros e desconto ao mesmo tempo")

        total = preco * quantidade

        if desconto > 0:
            total -= total * desconto

        if juros > 0:
            total += total * juros

        compra = {
            "preco": preco,
            "quantidade": quantidade,
            "forma": forma,
            "desconto": desconto,
            "juros": juros,
            "total": total
        }

        self.compras.append(compra)
        return compra

    def total_geral(self):
        return sum(c["total"] for c in self.compras)

    def resumo(self):
        return {
            "quantidade_compras": len(self.compras),
            "total_geral": self.total_geral()
        }