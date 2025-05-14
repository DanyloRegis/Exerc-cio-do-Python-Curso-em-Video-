lista = []
n1 = 0
while True:
    n = int(input("Digite um número inteiro positivo: "))
    n1 += 1
    lista.append(n)
    lista.sort(reverse=True)
    while True:
        continuar = str(input("Deseja continuar? [S/N] ")).upper()[0]
        if continuar == 'N':
            print("Saindo...")
            print(f"foram adicinados {n1} os numeros adicinados na Lista: {lista}")
            for v in lista:
                if v == 5:
                    print(f"o numero 5 esta ")
                else:
                    print(f"o numero 5 não esta ")
            exit()
        elif continuar == 'S':
            break
        else:
            print("Opção inválida! Digite S ou N.")
            continue