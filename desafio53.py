from unidecode import unidecode
texto = input("Digite uma palavra: ")

polindromo = unidecode(texto.replace(" ", "").strip().lower())  # Remove espaços

inverso = polindromo[::-1]

if polindromo == inverso:
    print(f"{texto} é um palíndromo")
else:
    print(f"{texto} não é um palíndromo")