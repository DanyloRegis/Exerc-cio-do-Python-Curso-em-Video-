

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))  
n3 = float(input('Digite mais um número: '))    

if n1 + n2 == n3 and n1 + n3 == n2 and n2 + n3 == n1:
    print('Os números formam um triângulo.')
else:
    print('Os números não formam um triângulo.')