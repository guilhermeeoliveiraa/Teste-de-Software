import json


class Produtos:
    def __init__(self, arquivo_db):
        self.arquivo_db = arquivo_db
        self._carregar()

    def _ler_arquivo(self):
        with open(self.arquivo_db, "r", encoding="utf-8") as f:
            return json.load(f)

    def _escrever_arquivo(self, dados):
        with open(self.arquivo_db, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=2, ensure_ascii=False)

    def _carregar(self):
        self.produtos = self._ler_arquivo()

    def _salvar(self):
        self._escrever_arquivo(self.produtos)

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