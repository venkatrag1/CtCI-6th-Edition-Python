from collections import defaultdict

def print_all_zero_sum_subarr(arr):
    sums = defaultdict(list, {0: [-1]})
    cum_sum = 0
    subarrs = []
    for i, num in enumerate(arr):
        cum_sum += num
        if len(sums[cum_sum]) > 0:
            for start in sums[cum_sum]:
                subarrs.append(arr[start+1:i+1])
        sums[cum_sum].append(i)
    return subarrs


#arr = [-3, 2, 3, 1, 6]
arr = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
n = len(arr)
print(print_all_zero_sum_subarr(arr))
