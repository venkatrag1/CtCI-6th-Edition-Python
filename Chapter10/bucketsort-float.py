def bucketSort(arr):
    num_buckets = 10
    buckets = [[] for bucket in range(num_buckets)]
    [buckets[int(num_buckets * x)].append(x) for x in arr]
    buckets = [sorted(bucket) for bucket in buckets]
    result = []
    for bucket in buckets:
        for x in bucket:
            result.append(x)
    return result



x = [0.897, 0.565, 0.656,
     0.1234, 0.665, 0.3434]
print("Sorted Array is")
print(bucketSort(x))

# This code is contributed by
# Oneil Hsiao