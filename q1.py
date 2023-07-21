def reverse_diagonals(matrix):
  n = len(matrix)
  for i in range(n // 2):
    j = n - i - 1
    matrix[i][i], matrix[j][j] = matrix[j][j], matrix[i][i]
    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

matrix = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
reverse_diagonals(matrix)
print(matrix)