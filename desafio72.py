x = ("um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez","onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
        n = int(input("Digite um número entre 1 e 20: "))
        if n < 1 or n > 20:
            print("Número fora do intervalo.", end=" ")
            continue
        else:
            print(f"Você digitou o número {x[n-1]}")
        while True:
            continuar = input("Deseja continuar? (s/n): ").strip().lower()
            if continuar == 's':
                break
            elif continuar == 'n':
                print("Programa encerrado.")
                exit()
            else:
                print("Opção inválida. Tente novamente.")