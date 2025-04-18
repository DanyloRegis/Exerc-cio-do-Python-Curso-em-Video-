#import math
# Desafio 06
n1=int(input("Digite um número: "))
n2=n1**2
n3=n1**3
#n4=math.sqrt(n1)
n4=n1**(1/2)
# n4=math.sqrt(n1) é a forma mais comum de calcular a raiz quadrada, mas o desafio pede para usar potência.
print(f"O quadrado de {n1} é {n2}, o cubo é {n3} e a raiz quadrada é {n4:.2f}.")