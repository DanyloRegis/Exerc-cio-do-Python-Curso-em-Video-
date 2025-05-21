from time import sleep

from random import randint



numeros = []



def sorteia(): 

    print('Sorteando 5 números:', end=' ')

    for _ in range(5):

        num = randint(1, 10)

        numeros.append(num)

        print(f'{num} ', end='', flush=True)

        sleep(0.3)

    print('\n')



def somaPar():

    soma = 0

    for num in numeros:

        if num % 2 == 0:

            soma += num

    print(f'A soma dos números pares sorteados é {soma}')



# Execução

sorteia()

somaPar()