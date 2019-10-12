"""
equal lengths -
Case 1- median A is less than median B- so u know 1/4 on left ; other 1/4 must lie
in the interval between medians

if equal - this is the median we're looking for

once u know which interval - mid pointof this 1/4 + 1/4

1/4 + 1/8 + 1/16 -> a ( 1 - r ^n ) / 1 - r; here 1/4 is a; 1/2 is rate
"""

def getMedian(arr1, arr2, n):
    if n == 0:
        raise ValueError("Empty array")
    if n == 1:
        return (arr1[0] + arr2[0]) / 2
    l1, l2 = 0, 0
    r1, r2 = n-1, n-1
    while n > 2:
        m1, m2 = median(arr1, l1, r1), median(arr2, l2, r2)
        if arr1[m1] == arr2[m2]:
            return arr1[m1]
        elif arr1[m1] > arr2[m2]:
            l2 = m2 + 1
            if (r2-l2+1) % 2 == 0: # Even so lies in middle so include on right side
                r1 = m1
            else: # odd so median can actually be ignored
                r1 = m1 - 1
        else:
            l1 = m1 + 1
            if (r2-l2+1) % 2 == 0: # Even so lies in middle so include on right side
                r2 = m2
            else:  # odd so median can actually be ignored
                r2 = m2 - 1
        n = n/2
    return (max(arr1[l1], arr2[l2]) + min(arr1[r1], arr2[r2])) / 2


def median(arr, start, end):
    m = start + int((end - start) / 2)
    return m


# Driver code
arr1 = [1, 2, 3, 6]
arr2 = [4, 6, 8, 10]
n = len(arr1)
print(int(getMedian(arr1, arr2, n)))
