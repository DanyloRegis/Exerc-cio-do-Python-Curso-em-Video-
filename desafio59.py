n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
lista = []
lista.append(n1)
lista.append(n2)
while True:
    try:
        print("Escolha uma operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. adicionar mais números")
        print("6. Sair")
        

        operacao = input("Digite o número da operação desejada: ")
        if operacao == "1":
                resultado = sum(lista)
                print(resultado)
                break
        elif operacao == "2":
                diferencas = [lista[i+1] - lista[i] for i in range(len(lista)-1)]
                print(diferencas)
                break
        elif operacao == "3":
                mutilcaso = [lista[i+1] * lista[i] for i in range(len(lista)-1)]
                print(mutilcaso)  
                break
        elif operacao == "4":
                divisao = [lista[i+1] / lista[i] for i in range(len(lista)-1)]
                print(divisao)
                break
        elif operacao == "5":
                n3 = float(input("Digite o terceiro número: "))
                lista.append(n3)
                print("Número adicionado com sucesso!")
        elif operacao == "6":
                print("Saindo...")
                break
    except ValueError:
        print("Por favor, digite um número válido.")
        continue