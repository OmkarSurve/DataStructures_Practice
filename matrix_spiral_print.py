"""
Print matrix in spiral order without any extra space
you are given a matrix of m x n elements (m rows, n columns),
Print all elements of the matrix in spiral order in O(m*n)
Time Complexity and O(1) Space Complexity Asked in : MicrosoftOLAPayTmOracle
"""


def spiral_print(r, c, matrix):

    k = n = 0
    m = c - 1
    p = r - 1

    while k < m and n < p:

        i = n
        for j in range(k, m):
            print (str(matrix[i][j]))

        j = m
        for i in range(n, p):
            print (str(matrix[i][j]))

        i = p
        for j in range(m, k, -1):
            print (str(matrix[i][j]))

        j = k
        for i in range(p, n, -1):
            print (str(matrix[i][j]))

        k += 1
        m -= 1
        n += 1
        p -= 1


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16],
          [17, 18, 19, 20]]

R = 5
C = 4
spiral_print(R, C, matrix)

