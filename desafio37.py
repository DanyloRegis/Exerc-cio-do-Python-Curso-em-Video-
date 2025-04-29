
# Desafio 37
while True:
    try:
        inicio = str(input("Quer iniciar a conversão? [Y/n] ")).strip().upper()
        if inicio == "N":
            print("Saindo...")
            break
        elif inicio != "Y":
            print("Opção inválida! Tente novamente.")
            continue
        else:
            num = int(input("Digite um número inteiro: "))
            escolha = int(input("Escolha uma base para conversão:\n"
                        "[1] Binário\n"
                        "[2] Octal\n"
                        "[3] Hexadecimal\n"
                        "Sua opção: "))
            if escolha == 1:
                print(f"{num} em binário é {bin(num)[2:]}")
            elif escolha == 2:
                print(f"{num} em octal é {oct(num)[2:]}")
            elif escolha == 3:
                print(f"{num} em hexadecimal é {hex(num)[2:]}")
            else:
                print("Opção inválida! Tente novamente.")
    except ValueError as e:
        print(f"Entrada inválida: {e}")