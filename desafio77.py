tupla = ("maçã", "banana", "laranja", "pêra", "abacaxi")
vogais = "aeiouáéíóúãõâêîôûAEIOUÁÉÍÓÚÃÕÂÊÎÔÛ"

print("Vogais em cada fruta:")
for fruta in tupla:
    vogais_fruta = [letra for letra in fruta if letra in vogais]
    print(f"{fruta}: {vogais_fruta} ({len(vogais_fruta)} vogais)")