def SortedMerge(A, B):
    j = len(B) - 1
    i = len(A) - len(B) - 1
    k = len(A) - 1
    while i >= 0 and j >= 0:
        if A[i] >= B[j]:
            A[k] = A[i]
            i -= 1
        else:
            A[k] = B[j]
            j -= 1
        k -= 1
    while j >=0:
        A[k] = A[j]
        j -= 1
        k -= 1
    return A



def FillArrayUpTo(maxnum):
    nums = [0] * maxnum
    for i in range(len(nums)):
        nums[i] = 2 * i + 4
    return nums


def FillArrayWithBuffer(length, buffer):
    nums = [0] * (length + buffer)
    for i in range(length):
        nums[i] = 3 * i + 1
    return nums

A = FillArrayWithBuffer(5, 10)
B = FillArrayUpTo(10)
print A, B
print SortedMerge(A, B)


"""
sad
das
fad
daf
"""