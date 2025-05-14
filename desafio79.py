lista = []
n = 0

while True  :
    n = int(input("Digite um número inteiro positivo: "))
    if n not in lista:
        lista.append(n)
        print("Adicionado na lista na posição")
        
    else:
        print("Número já existe na lista.")
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
