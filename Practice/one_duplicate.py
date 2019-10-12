def find_duplicate_sum(arr):
    n = len(arr) - 1
    expected_sum = (n * (n + 1)) / 2
    actual_sum = sum(arr)
    return actual_sum - expected_sum


def find_duplicate_xor(arr):
    n = len(arr) - 1
    xor = 0
    for num in range(1, n+1):
        xor ^=  num
    for num in arr:
        xor ^= num
    return xor

find_duplicate = find_duplicate_xor

print(find_duplicate([1,2,3,4,4]))
print(find_duplicate([1,2,3,4,2]))