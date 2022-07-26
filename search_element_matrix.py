"""
Problem: Matrix n*n is given, where all elements in any individual row or column are sorted.
In such a matrix, we have to find the position of a value in O(n) Time Complexity and O(1) Space Complexity

Algorithm: We start from the element 40 below, since 40 > 32, there is no point checking element from that column.
So we move left, now 30 < 32, so no point looking at elements in that row to left of 30, as they will be less than 30,
So we move down. Repeat this process till we find element. If element > search value move left if > move down.
"""


def searchElement(matrix, n, value):

    i = 0
    j = n - 1

    while i < n and j >= 0:

        if matrix[i][j] == value:
            print ("Search element at row index: " + str(i) + " and column index: " + str(j))
            return

        if matrix[i][j] > value:
            j -= 1
        else:
            i += 1

    print("Value not found")


matrix = [[10, 20, 30, 40],
          [15, 25, 36, 46],
          [28, 29, 37, 48],
          [32, 33, 39, 50]
]

n = 4
value = 33

searchElement(matrix, n, value)
