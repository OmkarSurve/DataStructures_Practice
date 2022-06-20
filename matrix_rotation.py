matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16],
          ]
n = 4


def matrix_rotation(matrix, n):

    for i in range(0, 2):
        for j in range(i, n-i-1):
            # At every step, we apply logic, column of source is row of destination and
            # column of destination is n - 1 - row of source
            t = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]    # j = n - x
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]  # i = n - 1 - x
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]   # n - 1 - j = n - 1 - x  n - 1 - n + 1 + j
            matrix[j][n - 1 - i] = t

    return matrix


print (matrix_rotation(matrix, n))
