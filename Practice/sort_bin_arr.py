def sort_binary_arr_linear(arr):
	l = 0
	r = len(arr) - 1
	done = False

	while not done:
		while l <= r and arr[l] == 0:
			l += 1
		while l <= r and arr[r] == 1:
			r -= 1
		if l >= r:
			done = True
		else:
			arr[l], arr[r] = arr[r], arr[l]
	return arr


print(sort_binary_arr_linear([1,0,1,0,1,0,0,1]))