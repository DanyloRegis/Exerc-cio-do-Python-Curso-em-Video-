import time
def voto(n):
    ano_atual = time.localtime().tm_year
    idade = ano_atual - n
    if idade < 16:
        return f"Com {idade} anos não se pode Votar "
    elif (idade == 16 or idade == 17) or idade >= 70:
        return f"Com {idade} anos não e obrigados a votar "
    else:
        return f"Com {idade} anos e obrigados a votar"

nasimento = int(input("Digite o ano que vc naceu "))
print(voto(nasimento))