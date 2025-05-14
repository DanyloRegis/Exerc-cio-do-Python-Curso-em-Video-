listaM = []
listaF = []

while True:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo (M)asculino (F)eminino (somente a primeira letra): ").upper()[0]
    
    # Validação dos dados
    if (sexo not in ["M", "F"]) or idade < 0 or idade > 120:
        print("Dados inválidos! Tente novamente.")
        continue
    
    # Adiciona às listas apropriadas
    if sexo == "M":
        listaM.append({"nome": nome, "idade": idade})
    else:
        listaF.append({"nome": nome, "idade": idade})
    
    # Pergunta se deseja continuar
    while True:
        sair = input("Você deseja sair? (S/N): ").upper()[0]
        if sair == "S":
            # Mostra resultados para homens
            print("\nHomens com 18 anos ou mais:")
            for homem in listaM:
                if homem["idade"] >= 18:
                    print(f"{homem['nome']} - {homem['idade']} anos")
            
            # Mostra resultados para mulheres
            print("\nMulheres com 18 anos ou mais:")
            for mulher in listaF:
                if mulher["idade"] >= 18:
                    print(f"{mulher['nome']} - {mulher['idade']} anos")
            
            # Mostra mulheres com menos de 20 anos
            print("\nMulheres com 19 anos ou menos:")
            for mulher in listaF:
                if mulher["idade"] < 20:
                    print(f"{mulher['nome']} - {mulher['idade']} anos")
            
            for homem in listaM:
                    print(f"Lista de homens completa: {homem['nome']} - {homem['idade']} anos")
            
            exit()  # Encerra o programa
        elif sair == "N":
            break  # Volta para o início do loop principal
        else:
            print("Opção inválida! Digite S ou N.")