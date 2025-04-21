def is_symmetric(matrix: list) -> bool:
    # Проверка на квадратность матрицы
    if len(matrix) == len(matrix[0]):
        for i in range(len(matrix)):    
            for j in range(len(matrix[0])):
                if not matrix[i][j] == matrix[j][i]: 
                    return False
        else:
            return True
    else:
        return False    


# Тест
matrix = [[1, 2, 3], 
          [2, 4, 5], 
          [3, 5, 6]]
print(is_symmetric(matrix))  # True

# Тест 2
matrix_two = [[1, 2, 3, 1], 
          [2, 4, 5, 2], 
          [3, 5, 6, 2],
          [1, 2, 3, 10]]

print(is_symmetric(matrix_two)) 