def desporcenoto(n, formato=True):
    x = n + (n * 0.1)
    return x if not formato else moeda(x)

def metade(n, formato=True):
    x = n / 2
    return x if not formato else moeda(x)

def dobro(n, formato=True):
    x = n * 2
    return x if not formato else moeda(x)

def moeda(n):
    return f"R${n:.2f}".replace('.', ',')

def line(a,b):
    print(f'{b}' * a )

def box_of_hashes(x):
    for i in range(x):
        print('#' * 10)

def square_of_hashes(x):
    for i in range(x):
        print('#' * x)

def square(x, y):
    for i in range(x):
        print(f'{y}' * x)

def triangle(x, y):
    for i in range(x):
        print(f'{y}' * i)

def shapes(a,b,c,d):
    for i in range(a):
        print(f'{b}' * i)
    for i in range(c):
        print(f'{d}' * a)

def spruce(size):
    print("a spruce!")
    
    # Print the tree
    for i in range(size):
        # Calculate the number of spaces and asterisks for the current level
        spaces = ' ' * (size - i - 1)
        asterisks = '*' * (2 * i + 1)
        print(spaces + asterisks)
    
    # Print the trunk of the tree
    trunk_spaces = ' ' * (size - 1)
    print(trunk_spaces + '*')

# Example usage:
spruce(3)
print()  # Just to separate the outputs
spruce(5)


if __name__ == "__main__":
    #line(20, '-')
    #box_of_hashes(5)
    #square(3, "ビル! ")
    #triangle(5, "🍺")
    shapes(5, "🍺", 3, "ビル! ")
    #print('Módulo de utilidades carregado com sucesso!')
    #line(20, '-')
    
    # Test the functions
    #print(desporcenoto(100))
    #print(metade(100))
    #print(dobro(100))
    #print(moeda(100))