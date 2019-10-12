def countSortASCII(arr):
    counts = [0] * 256
    output = [''] * len(arr)
    for c in arr:
        counts[ord(c)] += 1
    for i in range(1,len(counts)):
        counts[i] += counts[i-1]
    for c in arr:
        index = counts[ord(c)] - 1
        output[index] = c
        counts[ord(c)] -= 1
    return ''.join(output)


# # Driver program to test above function
# arr = "geeksforgeeks"
# ans = countSortASCII(arr)
# print "Sorted character array is %s" % ("".join(ans))


def countSort(arr, exp):
    count = [0] * 10
    output = [0] * len(arr)

    for x in arr:
        index = (x / exp) % 10
        count[index] += 1

    for i in range(1, len(count)):
        count[i] += count[i-1]

    for x in reversed(arr): # So that the higher index duplicates are treated with higher count- not needed for countSort but needed when used in radix sort
        index = (x / exp) % 10
        output[count[index] - 1] = x
        count[index] -= 1

    for i in range(len(output)):
        arr[i] = output[i]

    return arr


def radixSort(arr):
    max_val = max(arr)
    exp = 1

    while max_val / exp > 0:
        arr = countSort(arr, exp)
        exp *= 10

# Driver code to test above
arr = [ 170, 45, 75, 90, 802, 24, 2, 66]
radixSort(arr)

for i in range(len(arr)):
    print(arr[i]),
#O(d * (n + k)) - num passes * range plus number of digits