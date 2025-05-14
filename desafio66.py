n = s = 0 
lista = []
while True:
    n = int(input("Digite um número inteiro positivo (999 para parar): ")) 
    lista.append(n)
    s += n
    if n == 999:
        lista.remove(999)
        print("A lista de numeros digitados e :", end=" ")
        print(", ".join(map(str,lista)))
        print(f"A soma dos números é {s - 999}.")
        break