n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))    
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))
n5 = int(input("Digite o quinto número: "))
lista = (n1, n2, n3, n4, n5)
tres = noves = 0
pares = (i for i in lista if i % 2 == 0)  # Lista de números pares
print("Lista de numeros digitados :", ", ".join(map(str, lista)))  # Converte números para strings e junta com vírgulas
print("Lista de pares :", ", ".join(map(str, pares)))
for i in lista:
    if i == 9:
        noves += 1
        print(f"O número 9 apareceu {noves} vezes")
    if i == 3:
        tres += 1
        print(f"O número 3 apareceu {tres} vezes na lista na posicoa {lista.index(3)}")