def merge_arr(arr, l, m, r):
    s, e = l, m
    inv = 0
    temp_arr = []
    while s <= (m-1) and e <= r:
        if arr[s] > arr[e]:
            inv += (m - s)
            temp_arr.append(arr[e])
            e += 1
        else:
            temp_arr.append(arr[s])
            s += 1
    while s <= (m-1):
        temp_arr.append(arr[s])
        s += 1
    while e <= r:
        temp_arr.append(arr[e])
        e += 1
    for k in range(l, r+1):
        arr[k] = temp_arr[k-l]
    return inv



def count_array_inv_ms(arr, l, r):
    inv = 0
    if l < r:
        m = l + (r - l) // 2
        inv = count_array_inv_ms(arr, l, m)
        inv += count_array_inv_ms(arr, m+1, r)
        inv += merge_arr(arr, l, m+1, r)
    return inv



def count_array_inv(arr):
    return count_array_inv_ms(arr, 0, len(arr)-1)


# Driver Code
arr = [1, 20, 6, 4, 5]
n = len(arr)
print("Number of inversions are {}".format(
      count_array_inv(arr)))

"""
3:30

for every element count number of elements lower than that on the right side
O(N^2)

- modified merge sort - whenever inversion; everything greater will also be inverted
so get inversions from left and right 
and add merge step inverson
"""