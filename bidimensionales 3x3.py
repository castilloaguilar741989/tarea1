def search_value(matrix, value):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == value:
                return True, (i, j)
    return False, None

# Matriz de ejemplo
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# Valor a buscar
search_value = 5

found, position = search_value(matrix, search_value)

if found:
    print(f'El valor {search_value} se encontró en la posición {position}')
else:
    print(f'El valor {search_value} no se encontró en la matriz')
