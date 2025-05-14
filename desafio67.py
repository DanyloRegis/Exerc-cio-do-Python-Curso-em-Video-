n = 0
mutilicador = 0
while True:
    n = int(input("Digite um número inteiro positivo: "))
    if n <0:
        print("Numero negativo, fim de execução")
        break
    else:
            for i in range(11):
                mutiplicasao = n * i
                print(f"{n}x{i}={mutiplicasao}.")
                continue
