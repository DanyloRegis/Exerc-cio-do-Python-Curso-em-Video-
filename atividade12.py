
prduto = float(input("Digite o preço do produto: "))

if prduto <= 100:
    print(f"Preço com nao tem desconto") 
elif prduto > 100 and prduto <= 300:
    valor_desconto = prduto-(prduto * 0.05)
    print(f"Preço com desconto de 5%: {valor_desconto:.2f}")
else:
    valor_desconto = prduto-(prduto * 0.1)
    print(f"Preço com desconto de 10%: {prduto * 0.1:.2f}")