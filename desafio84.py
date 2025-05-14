lista = []
maior = menor = 0
pessoas_maior = pessoas_menor = []

while True:
    nome = str(input("Digite o Nome: "))
    peso = float(input("Digite o peso: "))
    lista.append([nome, peso])
    
    # Verifica maior e menor peso
    if len(lista) == 1:  # Primeiro cadastro
        maior = menor = peso
        pessoas_maior = [nome]
        pessoas_menor = [nome]
    else:
        if peso > maior:
            maior = peso
            pessoas_maior = [nome]
        elif peso == maior:
            pessoas_maior.append(nome)
            
        if peso < menor:
            menor = peso
            pessoas_menor = [nome]
        elif peso == menor:
            pessoas_menor.append(nome)

    while True:
        continuar = str(input("Deseja continuar? [S/N] ")).upper()[0]
        if continuar in 'SN':
            break
        print("Opção inválida! Digite S ou N.")

    if continuar == 'N':
        print("Saindo...")
        print(f"\nPessoas mais pesadas ({maior}kg): {', '.join(pessoas_maior)}")
        print(f"Pessoas mais leves ({menor}kg): {', '.join(pessoas_menor)}")
        print(f"Foram cadastradas {len(lista)} pessoas")
        break