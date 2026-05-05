from carrinho import Carrinho


def escolher_pagamento():
    print("\nForma de pagamento:")
    print("1 - PIX (5% desconto)")
    print("2 - Cartão (5% juros)")
    print("3 - Dinheiro (10% desconto)")

    opcao = input("Escolha: ")

    if opcao == "1":
        return "pix"
    elif opcao == "2":
        return "cartao"
    elif opcao == "3":
        return "dinheiro"
    else:
        print("Opção inválida!")
        return None


def executar():
    carrinho = Carrinho()

    while True:
        try:
            print("\n=== NOVA COMPRA ===")

            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade: "))

            forma = None
            while forma is None:
                forma = escolher_pagamento()

            compra = carrinho.adicionar_compra(preco, quantidade, forma)

            print("\n--- COMPRA ADICIONADA ---")
            print(f"Preço: R$ {compra['preco']:.2f}")
            print(f"Quantidade: {compra['quantidade']}")
            print(f"Forma: {compra['forma']}")

            if compra['desconto'] > 0:
                print(f"Desconto: {compra['desconto']*100:.0f}%")

            if compra['juros'] > 0:
                print(f"Juros: {compra['juros']*100:.0f}%")

            print(f"TOTAL: R$ {compra['total']:.2f}")
            print(f"TOTAL NO CARRINHO: R$ {carrinho.total_geral():.2f}")

            continuar = input("\nAdicionar outra compra? (s/n): ").lower()
            if continuar != "s":
                break

        except Exception as e:
            print(f"Erro: {e}")

    resumo = carrinho.resumo()
    print("\n=== RESUMO FINAL ===")
    print(f"Quantidade de compras: {resumo['quantidade_compras']}")
    print(f"Total geral: R$ {resumo['total_geral']:.2f}")


if __name__ == "__main__":
    executar()