def rotatedsearch(arr, key, l, r):
    if l <= r:
        m = l + int((r - l) / 2)
        if arr[m] == key:
            if m == 0 or arr[m-1] != arr[m]:
                return m
        if arr[m] > arr[l]: # Don't use elif it will ignore equal to case
            # Left is sorted
            if arr[m] >= key and arr[l] <= key:
                return rotatedsearch(arr, key, l, m - 1)
            else:
                return rotatedsearch(arr, key, m+1, r)
        elif arr[m] < arr[l]:
            # Right is sorted
            if arr[m] < key and arr[r] >= key:
                return rotatedsearch(arr, key, m+1, r)
            else:
                return rotatedsearch(arr, key, l, m-1)
        else:
            # Search both sides
            left_ind = rotatedsearch(arr, key, l, m-1)
            if left_ind == -1:
                return rotatedsearch(arr, key, m+1, r)
            else:
                return left_ind
    return -1


def shifted_arr_search(shiftArr, num):
  return shifted_arr_bin_search(shiftArr, num, 0, len(shiftArr)-1)

def shifted_arr_bin_search(shiftedArr, num, l, r):
  if l <= r:
    m = l + (r - l) // 2
    if shiftedArr[m] == num and ( m == 0 or shiftedArr[m-1] != shiftedArr[m]): # Same as above except one-liner
      return m
    elif shiftedArr[l] < shiftedArr[m]: # Left is in order
      if shiftedArr[l] <= num <= shiftedArr[m]:
        return shifted_arr_bin_search(shiftedArr, num, l, m-1)
      else:
        return shifted_arr_bin_search(shiftedArr, num, m+1, r)
    elif shiftedArr[l] > shiftedArr[m]: # Right is in sorted order
      if shiftedArr[m] < num <= shiftedArr[r]:
        return shifted_arr_bin_search(shiftedArr, num, m+1, r)
      else:
        return shifted_arr_bin_search(shiftedArr, num, l, m-1)
    else: # Search both sides
      left_ind = shifted_arr_bin_search(shiftedArr, num, l, m-1)
      if left_ind != -1:
        return left_ind
      return shifted_arr_bin_search(shiftedArr, num, m+1, r)
  return -1

print(rotatedsearch([9,12,17,2,4,5], 17, 0, 5))
print(shifted_arr_search([9,12,17,2,4,5], 17))