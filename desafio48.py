soma = 0
cont = 0
# Desafio 48    
for i in range(0, 500):
    if i % 3 == 0:
        print(i, end="\n")
        
        cont = cont + 1
        soma += i
print(f"a soma de todos os {cont} mutiplos de  3 e {soma}")