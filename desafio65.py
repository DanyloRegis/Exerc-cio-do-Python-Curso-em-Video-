soma = []
i = 0
while True:
    try:
        n = int(input("Digite um número inteiro positivo (999 para parar): "))
        i += 1
        soma.append(n)
        maior = max(soma) 
        menor = min(soma)
        media = sum(soma) / i
        final = input("Você deseja continuar? (Y/N): ").upper()
        if final == "N":
            print(f"A soma dos números é {sum(soma)}, o maior número é {maior}, o menor número é {menor} e a média é {media:.2f}.")
            break
        elif final == "Y":
            continue
        else:
            print("Opção inválida! Tente novamente.")
            continue
    except ValueError:
        print("Por favor, digite um número válido.")
        continue