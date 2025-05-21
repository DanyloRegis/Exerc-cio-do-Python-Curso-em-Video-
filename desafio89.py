lista = []

while True:
    n = str(input("Nome do aluno: "))
    n2 = float(input("Nota 1: "))
    n3 = float(input("Nota 2: "))
    
    # Adiciona o aluno e suas notas à lista
    lista.append([n, n2, n3])
    
    while True:
        continuar = str(input("Deseja continuar? [S/n] ")).upper()[0]
        if continuar == "S":
            break
        elif continuar == "N":
            # Exibe a média de cada aluno
            for index, (a, b, c) in enumerate(lista):
                media = (b + c) / 2
                print(f"{index} - Aluno: {a}, Média de notas: {media:.2f}")
            
            while True:
                try:
                    nota = int(input("Deseja ver as notas do aluno (Digite o número da posição do aluno)? "))
                    if 0 <= nota < len(lista):
                        aluno = lista[nota]
                        print(f"Aluno: {aluno[0]}, Nota 1: {aluno[1]}, Nota 2: {aluno[2]}")
                    elif nota == 999:
                        print("Finalizado....")
                        exit()
                    else:
                        print("Opção inválida. Tente novamente.")
                except ValueError:
                    print("Por favor, digite um número válido.")
            break
        else:
            print("Opção inválida. Tente novamente.")
