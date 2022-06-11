"""
Problem statement:
There are N children standing in a line with some rating value. You want to distribute a minimum number of
candies to these children such that:

Each child must have at least one candy.
The children with higher ratings will have more candies than their neighbours.
You need to write a program to calculate the minimum candies you must give.

Algo: We traverse the array twice, once from left and once from right
In first traversal, check if element at index[i+1] has rating greater than element at index[i],
in that case we increase the value by 1. and same for right traversal.
"""

rar = [1, 5, 2, 1]  # rating array given as input

car = [1] * len(rar)  # array to store number of candies

# Left traversal
for i in range(1, len(rar)):

    if rar[i] > rar[i-1]:
        car[i] = car[i] + 1

# Right traversal
for i in reversed(range(len(rar)-1)):

    if rar[i] > rar[i+1]:
        car[i] = car[i] + 1

print (sum(car))


