
def binarySearch(arr, start, end, val):
    if (start <= end):
        # If value is middle - return
        m = start + int((end - start) / 2)
        if val == arr[m]:
            return m
        elif val < arr[m]:
            return binarySearch(arr, start, m-1, val)
        else:
            return binarySearch(arr, m+1, end, val)
    return -1

# # Test array - binary search
# arr = [ 2, 3, 4, 10, 40 ]
# x = 15
#
# # Function call
# result = binarySearch(arr, 0, len(arr ) -1, x)
#
# if result != -1:
#     print "Element is present at index % d" % result
# else:
#     print "Element is not present in array"


def merge(arr, l, m, r):
    temparr = []
    i = l
    j = m+1
    while i <= m and j <= r:
        if arr[i] <= arr[j]:
            temparr.append(arr[i])
            i += 1
        else:
            temparr.append(arr[j])
            j += 1
    while i <= m:
            temparr.append(arr[i])
            i += 1
    while j <= r:
            temparr.append(arr[j])
            j += 1
    k = 0
    for i in range(l, r+1):
        arr[i] = temparr[k]
        k += 1
    return arr


    # Run over each and copy over smallest
    # Copy what's left of left subarray
    # Copy wha't left of right subarray
    # return merged array

def mergeSortHelper(arr, l, r):
    if l < r:
        m = l + int((r - l)/2)
        mergeSortHelper(arr, l, m)
        mergeSortHelper(arr, m+1, r)
        merge(arr, l, m, r)
    return arr

def mergeSort(arr):
    mergeSortHelper(arr, 0, len(arr)-1)

    # Check bounds
        # Get middle
        # Merge sort left array
        # Merge sort right array
        # Return Merge of two array




def printList(arr):
    for x in arr:
        print(x),


def partition(arr, l, r):
    pivot = l
    start = l + 1
    end = r
    done = False
    while not done:
        while arr[start] <= arr[pivot] and start <= end:
            start += 1
        while arr[end] >= arr[pivot] and start <= end:
            end -=1
        if start > end:
            done = True
        else:
            arr[start], arr[end] = arr[end], arr[start]
    arr[pivot], arr[end] = arr[end], arr[pivot]
    return end


def quickSortHelper(arr, l, r):
    if l < r:
        pivot = partition(arr, l, r)
        quickSortHelper(arr, l, pivot-1)
        quickSortHelper(arr, pivot+1, r)
    return arr

def quicksort(arr):
    quickSortHelper(arr, 0, len(arr)-1)

def insertionsort(arr):
    for i in range(1, len(arr)):
        curr_val = arr[i]
        curr_idx = i
        while curr_idx > 0 and arr[curr_idx-1] > curr_val:
            arr[curr_idx] = arr[curr_idx-1]
            curr_idx -= 1
        arr[curr_idx] = curr_val
    return arr

if __name__ == '__main__':
    sorter = insertionsort
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is")
    printList(arr)
    print("\n")
    sorter(arr)
    print("Sorted array is: ")
    printList(arr)

    # This code is contributed by Mayank Khanna
