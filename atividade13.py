nota = int(input("Digite a nota (0–100): "))
if 90 <= nota <= 100:
    conceito = "A"
elif 75 <= nota <= 89:
    conceito = "B"
elif 60 <= nota <= 74:
    conceito = "C"
elif 40 <= nota <= 59:
    conceito = "D"
else:
    conceito = "F"
print(f"Conceito: {conceito}")
