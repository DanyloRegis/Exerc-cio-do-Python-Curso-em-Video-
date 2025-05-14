lista = []
par = []
impar = []

while True:
    n = int(input("Digite um número inteiro positivo: "))
    lista.append(n)
    lista.sort()
    while True:
        continuar = str(input("Deseja continuar? [S/N] ")).upper()[0]
        if continuar == 'N':
            for i in lista:
                if i % 2 == 0:
                    par.append(i)
                    par.sort()
                else:
                    impar.append(i)
                    impar.sort()
            print("Saindo...")
            print(f" os numeros adicinados na Lista: {lista}")
            print(f" os numeros adicinados na Lista: {par}")
            print(f" os numeros adicinados na Lista: {impar}")
            exit()
        elif continuar == 'S':
            break
        else:
            print("Opção inválida! Digite S ou N.")
            continue