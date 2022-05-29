"""
array = [2, 1, 1, 0, 1, 2, 1, 2, 0, 0, 1]
Array consist of only 0's, 1's and 2's. Write an algorithm to sort  this array in O(n) time complexity and O(1)
Space complexity with only one traversal Asked in : AmazonMicrosoftAdobeWalmartLabs
"""

ar = [1, 0, 1, 0, 1, 2, 1, 2, 0, 0, 2]

low = 0
mid = 0
high = len(ar) - 1

while mid <= high:

    # if mid is pointing to value 2 swap the value at index high with 2
    if ar[mid] == 2:
        t = ar[high]
        ar[high] = ar[mid]
        ar[mid] = t
        high = high - 1
    elif ar[mid] == 1:
        mid += 1
    else:
        t = ar[low]
        ar[low] = ar[mid]
        ar[mid] = t
        low += 1
        mid += 1


print(ar)

