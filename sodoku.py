sodoku =[   [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]]

def is_valid(sodoku, row, col, value):
    for i in range(9):
        if sodoku[row][i] == value or sodoku[i][col] == value:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if sodoku[i][j] == value:
                return False
    return True


def print_sudoku(sodoku):
    for row in sodoku:
        print(" ".join(str(num) if num != 0 else '-' for num in row))
while True:
    print_sudoku(sodoku)
    print("Preencha o Sudoku:")
    try:
        linha  = int(input("Digite a linha (1-9): "))-1
        coluna = int(input("Digite a coluna (1-9): "))-1
        valor = int(input("Digite o valor (1-9): "))
        
        if 0 <= linha < 9 and 0 <= coluna < 9 and 1 <= valor <= 9:
            if is_valid(sodoku, linha, coluna, valor):
                sodoku[linha][coluna] = valor
            else:
                print("Essa posição já está preenchida.")
            continuar = input("Deseja continuar? (s/n): ").lower()
            if continuar != 's':
                break
        else:
            print("Posição ou valor inválido. Tente novamente.")
    except ValueError:
        print("Por favor, insira um número válido.")