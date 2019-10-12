def searchLeft(arr, val, l, r):
    if l <= r:
        m = l + int((r-l) / 2)
        if arr[m] == val and (m == 0 or arr[m-1] != arr[m]):
            return m
        elif arr[m] >= val:
            return searchLeft(arr, val, l, m-1)
        else:
            return searchLeft(arr, val, m+1, r)
    return -1


def searchRight(arr, val, l, r):
    if l <= r:
        m = l + int((r-l) / 2)
        if arr[m] == val and (m == (len(arr)-1) or arr[m+1] != arr[m]):
            return m
        elif arr[m] <= val:
            return searchRight(arr, val, m+1, r)
        else:
            return searchRight(arr, val, l, m-1)
    return -1

def count(arr, val, n):
    left_ind = searchLeft(arr, val, 0, n-1)
    if left_ind == -1:
        return 0
    right_ind = searchRight(arr, val, 0, n-1)
    print(left_ind, right_ind)
    return right_ind - left_ind + 1




# driver program to test above functions
arr = [1, 2, 2, 3, 3, 3, 3]
x = 3  # Element to be counted in arr[]
n = len(arr)
c = count(arr, x, n)
print ("%d occurs %d times "%(x, c))

"""
9:02 - 9:31
"""