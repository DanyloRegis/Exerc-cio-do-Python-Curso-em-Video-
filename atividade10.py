

cpf = int(input("Digite o CPF:(apenas os numeros) "))

if len(str(cpf)) == 11 and cpf.isnumeric():
    print("CPF válido")
    if cpf.startwoth("0"):
        print("CPF inválido")
else:   
    print("CPF inválido")