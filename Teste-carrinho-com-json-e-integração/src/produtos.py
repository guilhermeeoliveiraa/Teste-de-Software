import json

class Produtos:
    def __init__(self, arquivo_db):
        self.arquivo_db = arquivo_db
        self._carregar()

    def _carregar(self):
        with open(self.arquivo_db, "r", encoding="utf-8") as f:
            self.produtos = json.load(f)

    def _salvar(self):
        with open(self.arquivo_db, "w", encoding="utf-8") as f:
            json.dump(self.produtos, f, indent=2)

    def buscar_por_id(self, id_produto):
        for p in self.produtos:
            if p["id"] == id_produto:
                return p
        return None

    def atualizar_estoque(self, id_produto, quantidade):
        produto = self.buscar_por_id(id_produto)
        if not produto:
            raise ValueError("Produto não encontrado")

        if produto["quantidade"] < quantidade:
            raise ValueError("Estoque insuficiente")

        produto["quantidade"] -= quantidade
        self._salvar()
        return produto

    def cadastrar(self, produto):
        self.produtos.append(produto)
        self._salvar()