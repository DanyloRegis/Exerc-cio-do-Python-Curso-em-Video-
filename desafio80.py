# Lista original
lista = []

while True:

    numero = int(input("Digite um número para inserir na lista: "))

    # Inserir o número na posição correta
    for i in range(len(lista)):
        if numero < lista[i]:
            lista.insert(i, numero)
            print(f"Adicionado na lista na posição {i}")
            break
    else:
        # Se o número for maior que todos os elementos, adiciona ao final
        lista.append(numero)
        print(f"Adicionado na lista na posição {i}")
    while True:
        continuar = str(input("Deseja continuar? [S/N] ")).upper()[0]
        if continuar == 'N':
            print("Saindo...")
            print(f"os numeros adicinados na Lista: {sorted(lista)}")
            exit()
        elif continuar == 'S':
            break
        else:
            print("Opção inválida! Digite S ou N.")
            continue
