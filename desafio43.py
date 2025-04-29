tamanho = float(input("Digite o tamanho em metros: "))
peso = float(input("Digite o peso em kg: "))
imc = peso / (tamanho ** 2)

print(f"Seu IMC é: \033[1m{imc:.1f}\033[0m")

if imc < 18.5:
    print("\033[33mAbaixo do peso\033[0m")
elif 18.5 <= imc < 25:      
    print("\033[32mPeso normal\033[0m")
elif 25 <= imc < 30:
    print("\033[33mSobrepeso\033[0m")
elif 30 <= imc < 35:
    print("\033[31mObesidade grau I\033[0m")
elif 35 <= imc < 40:
    print("\033[31mObesidade grau II\033[0m")   
elif imc >= 40:
    print("\033[31mObesidade grau III\033[0m")
else:
    print("\033[31mObesidade grau IV\033[0m")