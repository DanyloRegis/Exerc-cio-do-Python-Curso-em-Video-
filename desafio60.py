while True:
    try:
        n1 = int(input("Digite o primeiro número: "))
        
        if n1 < 0:
            print("Número inválido! Tente novamente.")
            continue  # Volta para o início do loop para pedir um novo número
        elif n1 == 0:
            print("O fatorial de 0 é 1")
            break
        elif n1 == 1:
            print("O fatorial de 1 é 1")
            break
        else:
            fatorial = 1
            for i in range(1, n1 + 1):
                fatorial *= i
            print(f"O fatorial de {n1} é {fatorial}")
            break
    except ValueError:
        print("Por favor, digite um número válido.")
