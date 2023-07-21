def count_submatrix_occurrences(matrix_A, submatrix_B):
    rows_A, cols_A = len(matrix_A), len(matrix_A[0])
    rows_B, cols_B = len(submatrix_B), len(submatrix_B[0])

    count = 0

    for row in range(rows_A - rows_B + 1):
        for col in range(cols_A - cols_B + 1):
            found = True
            for i in range(rows_B):
                for j in range(cols_B):
                    if matrix_A[row + i][col + j] != submatrix_B[i][j]:
                        found = False
                        break
                if not found:
                    break

            if found:
                count += 1

    return count


# Exemplo de uso:
A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 8, 7, 6],
    [5, 4, 3, 2]
]

B = [
    [3, 4],
    [7, 8]
]

result = count_submatrix_occurrences(A, B)
print(result)  # Saída: 1, pois a submatriz B ocorre uma vez na matriz A.
