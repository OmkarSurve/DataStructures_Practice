"""

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the
non-zero elements in O(n) Time complexity and O(1) Space complexity with single traversal allowed
ar = [1, 3, 0, 0, 4, 0, 9]
"""

ar = [0, 0, 1, 2, 0, 4]
low = 0  # point to right of left most non zero index. Will be incremented if we encounter non zero value.
mov = 0  # point to current position while traversing the array. WIll be incremented every time.

while mov < len(ar):
    if ar[mov] != 0:
        if low == mov:
            low += 1
            mov += 1
        else:
            t = ar[low]
            ar[low] = ar[mov]
            ar[mov] = t
            low += 1
            mov += 1
    else:
        mov += 1

print(ar)
