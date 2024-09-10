from biblioteca import cpf_valido

def caixa_de_mercado():
    lista_produtos = [
        "Arroz", "Feijão", "Macarrão", "Óleo", "Açúcar",
        "Sal", "Café", "Leite", "Queijo", "Presunto",
        "Pão", "Manteiga", "Frango", "Carne", "Peixe",
        "Maçã", "Banana", "Laranja", "Cebola", "Tomate",
        "Batata", "Cenoura", "Alho", "Papel Toalha", "Detergente",
        "Sabão", "Xampu", "Condicionador", "Creme Dental", "Desodorante"
    ]

    lista_precos = [
        10.50, 8.20, 4.30, 7.90, 3.50,
        1.50, 15.00, 5.60, 22.00, 18.00,
        3.00, 9.40, 12.80, 25.60, 20.00,
        2.00, 2.50, 3.80, 4.50, 6.20,
        2.20, 3.00, 1.80, 1.50, 5.00,
        6.50, 4.20, 7.30, 8.10, 10.00
    ]

    produtos = {}
    for i in range(len(lista_produtos)):
        produtos[i] = {"nome": lista_produtos[i], "preco": lista_precos[i]}

    while True:
        cpf = input("Digite o CPF (11 dígitos): ")
        validacao = cpf_valido(cpf)
        if validacao == "CPF válido.":
            print(validacao)
            break
        else:
            print(validacao)
            continue

    print("\nBem-vindo ao Mercado! Aqui estão os produtos disponíveis:")
    for i in produtos:
        print(f"{i} - {produtos[i]['nome']}: R$ {produtos[i]['preco']:.2f}")

    total = 0
    produtos_selecionados = []

    while True:
        indice = input("\nDigite o índice do produto que deseja adicionar (ou 'sair' para encerrar): ")
        if indice.lower() == 'sair':
            break

        try:
            indice = int(indice)
            if indice in produtos:
                quantidade = int(input(f"Digite a quantidade de {produtos[indice]['nome']} que deseja adicionar: "))
                produto = produtos[indice]["nome"]
                preco = produtos[indice]["preco"] * quantidade
                total += preco
                produtos_selecionados.append((produto, quantidade, preco))
                print(f"{quantidade}x {produto} adicionado(s). Total atual: R$ {total:.2f}")
            else:
                print("Índice inválido, tente novamente.")
        except ValueError:
            print("Por favor, digite um número válido ou 'sair'.")

    # Gera nota fiscal
    print("\n--- Nota Fiscal ---")
    print(f"CPF do cliente: {cpf}")
    print("Produtos comprados:")
    for produto, quantidade, preco in produtos_selecionados:
        print(f"- {quantidade}x {produto}: R$ {preco:.2f}")
    print(f"\nTotal a pagar: R$ {total:.2f}")
    print("-------------------")

if __name__ == "__main__":
    caixa_de_mercado()