def count(arr, m, n):
    cache = [0 for k in range(n+1)]
    cache[0] = 1
    for i in range(m):
        for j in range(arr[i], n+1):
            cache[j] += cache[j-arr[i]]
    return cache[n]




# Driver program to test above function
arr = [1, 2, 3]
m = len(arr)
n = 4
x = count(arr, m, n)
print (x)


