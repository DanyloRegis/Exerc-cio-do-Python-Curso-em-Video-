
while True:
    n = input("Digite Seu sexo (M)asculino (F)eminino (somente a primeira letra): ").upper()
    if n == "M":
        print("Você é do sexo masculino.")
        break
    elif n == "F":
        print("Você é do sexo feminino.")
        break
    else:
        print("Opção inválida! Tente novamente.")
        continue