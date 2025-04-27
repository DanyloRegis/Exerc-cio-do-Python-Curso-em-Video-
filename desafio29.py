
carro = float(input("Qual a velocidade do carro? "))

if carro > 80:
    multa = (carro - 80) * 7
    print(f"Você foi multado em R$ {multa:.2f} por excesso de velocidade.") 
else:
    print("Você não foi multado.")
