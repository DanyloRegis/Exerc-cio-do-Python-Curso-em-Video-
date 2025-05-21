def area():
    largura = float(input("Digite a largura: "))
    comprimento = float(input("Digite o comprimento: "))
    area = largura * comprimento
    print(f"A área é: {area}")
    return area

# Chamando a função
area()