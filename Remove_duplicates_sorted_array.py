"""
Remove duplicates from the sorted array
v = temp variable
j = pointer to which distinct value to write
Algo: Move distince values to left
"""

arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]


def remove_dup(ar):

    v = ar[0]
    j = 0

    for i in range(1, len(ar)):

        if ar[i] == v:
            continue
        else:
            j += 1
            ar[j] = ar[i]
            v = ar[i]

    return ar[0:j+1], j + 1


print (remove_dup(arr))

