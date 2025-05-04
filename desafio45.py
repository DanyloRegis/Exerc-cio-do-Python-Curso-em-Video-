import random



while True:
    try:
        vai_jogar = str(input("Quer jogar Jokenpô? [Y/n] ")).strip().upper()
        if vai_jogar == "N":
            print("Saindo...")
            break
        elif vai_jogar != "Y":
            print("Opção inválida! Tente novamente.")
            continue
        else:
            print("Vamos jogar!")
            jakenpo = {
                0: 'Pedra',
                1: 'Papel',
                2: 'Tesoura'
                }       
            pc_escolha = random.randint(0, 2)
            print("Escolha uma opção:")
            print("[0] Pedra")
            print("[1] Papel")
            print("[2] Tesoura")
            usuario_escolha = int(input("Sua escolha: "))

            if usuario_escolha not in jakenpo:
                raise ValueError("Opção inválida! Tente novamente.")

            print(f"Você escolheu: {jakenpo[usuario_escolha]}")
            print(f"Computador escolheu: {jakenpo[pc_escolha]}")

            if usuario_escolha == pc_escolha:
                print("Empate!")
            elif (usuario_escolha == 0 and pc_escolha == 2) or \
                    (usuario_escolha == 1 and pc_escolha == 0) or \
                    (usuario_escolha == 2 and pc_escolha == 1):
                print("Você ganhou!")
            else:
                print("Você perdeu!")

            continuar = input("Deseja jogar novamente? [Y/n] ").strip().upper()
            if continuar == 'N':
                break

    except ValueError as e:
        print(f"Entrada inválida: {e}")