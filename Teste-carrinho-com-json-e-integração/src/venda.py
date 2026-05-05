def processar_venda(produtos_repo, pagamento, id_produto, quantidade, forma):
    produto = produtos_repo.buscar_por_id(id_produto)

    if not produto:
        raise ValueError("Produto não encontrado")

    if produto["preco"] <= 0:
        raise ValueError("Preço inválido")

    total = pagamento.calcular_total(produto["preco"], quantidade, forma)

    produtos_repo.atualizar_estoque(id_produto, quantidade)

    resultado = pagamento.pagar(total)

    return {
        "produto": produto["nome"],
        "total": total,
        "status": resultado["status"]
    }