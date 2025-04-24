

texto = str(input("Digite o texto: "))
contador = texto.count("a") + texto.count("A")
print(f"O número de letras 'a' ou 'A' no texto é: {contador} e sua aultimam ocorrência é na posição {texto.rfind('a') if texto.rfind('a') > -1 else texto.rfind('A')}")