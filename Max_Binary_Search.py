"""
One array of integers is given as an input ,which is initially increasing and then decreasing or it can be only increasing or decreasing , 
you need to find the maximum value in the array in O(Log n) Time complexity and O(1) Space Complexity Asked in : AmazonMicrosoftUber
"""

"""
Input: array[] = {3, 5,15, 50, 11, 10, 8, 6}
{3, 5, 20, 15, 14, 13, 12, 11}
{2, 3, 5, 7, 9, 10, 8}
"""


def max_bin(ar, low, high):

    if ar[low] == ar[high]:
        return ar[low]

    if high == low + 1:
        if ar[high] > ar[low]:
            return ar[high]

        return ar[low]

    mid = low + (high-low)//2

    if (ar[mid-1] < ar[mid]) and (ar[mid] > ar[mid+1]):
        return max_bin(ar, low, mid)
    elif ar[mid-1] < ar[mid] < ar[mid+1]:
        return max_bin(ar, mid+1, high)
    else:
        return max_bin(ar, low, mid-1)


if __name__ == '__main__':

    ar = [14, 10, 9, 8, 6, 4, 2]
    low = 0
    high = len(ar) - 1

    print (max_bin(ar, low, high))


