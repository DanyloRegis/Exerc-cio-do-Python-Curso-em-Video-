

idade = int(input("Digite o ano de nascimento: "))

if idade < 8:
    print(f"Você tem {idade} anos e está na categoria mirim.")
elif idade >= 8 and idade < 11: 
    print(f"Você tem {idade} anos e está na categoria infantil.")
elif idade >= 11 and idade < 14:
    print(f"Você tem {idade} anos e está na categoria juvenil.")
elif idade >= 14 and idade < 17:
    print(f"Você tem {idade} anos e está na categoria junior.")
elif idade >= 17 and idade < 20:
    print(f"Você tem {idade} anos e está na categoria senior.")
elif idade >= 20:
    print(f"Você tem {idade} anos e está na categoria master.")