"""
You have an array of non-negative integers,you are initially positioned at the first index of the array.Each element in
the array represents your maximum jump length at that position.Determine if you are able to reach the last index in O(n)
Time complexity and O(1) Space Complexity Asked in : AdobeIntuit
"""
"""
Hera a points to the jump remaining. B moves along which helps in deciding next jump value.
eg. below, jump at 3. At index 3 a becomes 0. B becomes 2 which is given to a.
Next jump at index 5, b becomes 3, so a becomes 3. During 4th Jump at index 7, value of b becomes 7.
So at index 8 when a becomes 0, b becomes 6 which makes a 6. and we reach last element. So 4 jumps
"""

arr = [3, 4, 2, 2, 4, 3, 1, 7, 3, 7, 1, 8, 2, 4]


def short_jump(arr):

    a = arr[0]
    b = arr[1] + 1
    jump = 0

    if arr[0] == 0:
        return -1

    if len(arr) == 1:
        return 1

    for i in range(1, len(arr)):

        a -= 1
        b -= 1
        if b < arr[i]:
            b = arr[i]

        if a == 0:
            jump += 1
            a = b
            print (i)

    return jump + 1


print(short_jump(arr))







