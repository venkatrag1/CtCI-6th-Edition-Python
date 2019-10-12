

def zero_sum_exists(arr):
	sums = set()
	cum_sum = 0
	for num in arr:
		cum_sum += num
		if cum_sum in sums:
			return True
		sums.add(cum_sum)
	return False


#arr = [-3, 2, 3, 1, 6]
arr = [4, 2, -3, 1, 6]
n = len(arr)
if zero_sum_exists(arr) == True:
    print("Found a sunbarray with 0 sum")
else:
    print("No Such sub array exits!")

    # This code is contributed by Shrikant13