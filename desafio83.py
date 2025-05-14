lista = []
n = str(input("Digite uma formula "))
for i in lista:
    if i == "(":
        lista.append(i)
    elif i == ")":
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(i)
if len(lista) == 0:
    print("A formula é válida") 
else:
    print("A formula é inválida")
    