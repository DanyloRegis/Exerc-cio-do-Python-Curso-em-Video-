serie_a = ("Palmeiras", "Bragantino", "Flamengo", "Cruzeiro", "Fluminense", 
           "Bahia", "Ceará", "Corinthians", "Internacional", "Atlético-MG",
           "São Paulo", "Botafogo", "Grêmio", "Vasco", "Juventude",
           "Mirassol", "Fortaleza", "Vitória", "Santos", "Sport","Chapecoense")

# Imprime os 6 primeiros times
print("top 5\n")
for i in range(5):
    print(serie_a[i], end=", ")
print("\n5 últimos")
for i in range(15, 20):
    print(serie_a[i], end=", ")
print("lista em ordem alfabética")
for i in sorted(serie_a):
    print(i, end=",")
print("\nChapecoense esta na lista?")
if "Chapecoense" in serie_a:
    print(f"Sim, o Chapecoense está na posição {serie_a.index('Chapecoense') + 1}")
else:
    print("Não, o Chapecoense não está na lista")