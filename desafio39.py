
ano_nasimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade = ano_atual - ano_nasimento
sexo = str(input("Digite seu sexo [M/F]: ")).strip().upper()

if sexo not in ['M', 'F']:
    print("Sexo inválido! Tente novamente.")
    sexo = str(input("Digite seu sexo [M/F]: ")).strip().upper()
else:
    if sexo == 'M':
        if idade < 18:
            print(f"Você tem {idade} anos e ainda não pode se alistar. falta {18-idade} anos para se alistar.")
        elif idade == 18:
            print(f"Você tem {idade} anos e deve se alistar.")
        else:
            print(f"Você tem {idade} anos e já deveria ter se alistado.")
    elif sexo == 'F':
        print("Você é do sexo feminino. vc não precisa se alistar .")