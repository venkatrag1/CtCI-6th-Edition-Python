def binarySearch(arr, val):
    start = 0
    end = len(arr) - 1
    while start <= end:
        m = start + int((end - start) / 2)
        if arr[m] == val:
            return True
        elif arr[m] < val:
            start = m + 1
        else:
            end = m - 1
    return False


def find_duplicates(arr1, arr2):
    N = min(len(arr1), len(arr2))
    M = max(len(arr1), len(arr2))
    if N == len(arr1):
        a1, a2 = arr1, arr2
    else:
        a1, a2 = arr2, arr1
    result = []
    if int(M / 2) <= N <= M:
        # near equal size
        i, j = 0, 0
        while i < N and j < M:
            if a1[i] == a2[j]:
                result.append(a1[i])
                i += 1
                j += 1
            elif a1[i] < a2[j]:
                i += 1
            else:
                j += 1
    else:

        for i in range(N):
            if binarySearch(a2, a1[i]):
                result.append(a1[i])
    return result
    # M is much larger




arr1 = [1, 2, 3, 5, 6, 7]
arr2 = [3, 6, 7, 8, 20]

print(find_duplicates(arr2, arr1))
output= [3, 6, 7]

assert find_duplicates(arr2, arr1) == output
