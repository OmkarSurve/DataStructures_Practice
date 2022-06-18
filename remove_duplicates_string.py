str_a = 'abrakadabra'


def remove_dup(arr):

    ascii_a = [0] * 256
    p = ''

    for i in arr:

        if ascii_a[ord(i)] == 0:
            ascii_a[ord(i)] = -1
            p = p + i
        elif ascii_a[ord(i)] == -1:
            continue

    return p


print(remove_dup(str_a))