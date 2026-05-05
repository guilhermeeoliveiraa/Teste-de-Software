class BancoAPI:
    def processar(self, valor):
        # simulação simples
        return {"status": "aprovado", "valor": valor}


class Pagamento:
    def __init__(self, banco_api):
        self.banco = banco_api

    def calcular_total(self, preco, quantidade, forma):
        total = preco * quantidade

        if forma == "pix":
            total *= 0.95
        elif forma == "cartao":
            total *= 1.05
        elif forma == "dinheiro":
            total *= 0.90
        else:
            raise ValueError("Forma inválida")

        return total

    def pagar(self, valor):
        return self.banco.processar(valor)