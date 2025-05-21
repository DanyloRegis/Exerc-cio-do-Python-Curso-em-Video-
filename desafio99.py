def maior():
    lista = []
    while True:
        n = int(input("Digite um numero: "))
        lista.append(n)
        while True:
            final = str(input("Quer continuar S/n ")).upper()[:]
            if final == 'N':
                print(f"O maior numero {max(lista)} menor numeoro {min(lista)}")
                exit()
            else:
                break

maior()