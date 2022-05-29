"""
We rotate an ascending order sorted array at some point unknown to user. So for instance, 3 4 5 6 7 might become 5 6 7 3 4. 
Modify binary search algorithm to find an element in the rotated array in O(log n) time and O(1) Space complexity
"""

"""
array[] = {3,4,5,6,7,8,9,10,1,2}
array[] = {9,10,1,2,3,4,5,6,7,8}
array[] = {7,8,9,10,1,2,3,4,5,6}
Search Number = 1
"""

def bin_rot(ar, key, low, high):
    
    # Base case
    if low > high:
        return -1

    mid = low + (high-low)//2

    if ar[mid] == key:
        return mid

    if ar[low] <= ar[mid]:
        if key <=ar [mid] and key >= ar[low]:
            return bin_rot(ar, key, low, mid)
        else:
            return bin_rot(ar, key, mid+1, high)

    else:
        if key >= ar[mid+1] and key <=ar[high]:
            return bin_rot(ar, key, mid+1, high)
        else:
            return bin_rot(ar, key, low, mid)


if __name__ == '__main__':

    ar = [9,10,1,2,3,4,5,6,7,8]
    key = 10    # Element to be searched

    print(bin_rot(ar, key, 0, len(ar)-1))
