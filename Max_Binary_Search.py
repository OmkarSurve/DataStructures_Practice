"""
Input: array[] = {3, 5,15, 50, 11, 10, 8, 6}
{3, 5, 20, 15, 14, 13, 12, 11}
{2, 3, 5, 7, 9, 10, 8}
"""


def max_bin(ar, low, high):
    
    # End case
    if ar[low] == ar[high]:
        return ar[low]
    
    # End case
    if high == low + 1:
        if ar[high] > ar[low]:
            return ar[high]

        return ar[low]
    
    # Divide the array till we get the end case
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





