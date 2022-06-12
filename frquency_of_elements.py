"""
Count frequencies of array elements in O(n) time complexity and O(1) space complexity

Problem statement: Array of length n having integers 1 to n with some elements being repeated.
Count frequencies of all elements from 1 to n Asked in : PayTm, VmWare, Amazon
Algorithm: eg. array of lenght 7 with values between 1 to 7. When we find the element i we add 8 to the element at index i
Finally based on % and // operator we calculate the frequency. Element with values less that 8 has frequency of zero
"""


def len_arr(ar):

    for i in ar:
        if i < 8:
            ar[i-1] = ar[i-1] + 8
        else:
            o = i % 8
            ar[o-1] = ar[o-1] + 8


ar = [1, 4, 2, 5, 3, 7, 2]

len_arr(ar)

n = 2
print ("Frequency of " + str(n) + " is: " + str(ar[n-1] // 8))
