soma = []
while True:
    try:
        n = int(input("Digite um número inteiro positivo (999 para parar): "))
        if n == 999:
            print("Os números digitados foram:")
            print(",".join(map(str, soma)))  # Convertendo números para strings
            print(f"A soma dos números digitados é {sum(soma)}")
            break
        soma.append(n)
    except ValueError:
        print("Por favor, digite um número válido.")