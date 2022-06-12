"""
Print Matrix Diagonally
Given a matrix of M x N elements (M rows, N columns),
Print all elements of the matrix in diagonal order in Time Complexity O(m*n) and Space Complexity O(1)
The trick is when we print next element we usually print mat[i][j] > mat[i-1][j+1] until row <= 0 and col < max_column
"""


def diagonal_matrix(r, c, matrix):

    for i in range(r):

        k = i
        j = 0
        while k >= 0 and j <= i:
            print(matrix[k][j])
            k -= 1
            j += 1

    for i in range(1, c):

        k = r - 1
        j = i
        while k >= 0 and j <= c - 1:
            print(matrix[k][j])
            k -= 1
            j += 1


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16],
          ]

R = 4
C = 4
diagonal_matrix(R, C, matrix)