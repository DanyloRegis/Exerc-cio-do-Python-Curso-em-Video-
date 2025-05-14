lista = []
n = 0
custo = 0.0

while True:
    nome = input("Digite o nome do produto: ")
    valor = float(input("Digite o valor: "))
    lista.append({"produto": nome, "valor": valor})
    n += 1
    custo += valor
    total = custo / n

    # Pergunta se deseja continuar
    while True:
        sair = input("Você deseja sair? (S/N): ").upper()[0]
        if sair == "S":
            print("\n--- Relatório Final ---")
            for produto in lista:
                if produto["valor"] > 1000:
                    print(f"Produto acima de R$1000: {produto['produto']}, Valor: R${produto['valor']:.2f}")

            print(f"Custo total: R${custo:.2f}")
            print(f"Média de custo: R${total:.2f}")

            # Produto com menor valor
            menor_valor = min(lista, key=lambda x: x["valor"])
            print(f"Produto mais barato: {menor_valor['produto']} - R${menor_valor['valor']:.2f}")
            exit()
        elif sair == "N":
            break  # Continua o loop principal
        else:
            print("Opção inválida! Digite S ou N.")
