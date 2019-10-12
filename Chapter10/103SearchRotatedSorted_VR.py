import pytest

def rotatedsearch(arr, key, l, r):
    if l <= r:
        m = l + int((r - l) / 2)
        if arr[m] == key:
            if m == 0 or arr[m-1] != arr[m]:
                return m
        if arr[m] > arr[l]:
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

#7.22
def get_index(arr, key):
    return rotatedsearch(arr, key, 0, len(arr)-1)

@pytest.mark.parametrize("arr,key,ind",
[
 ([4, 5, 6, 7, 8, 9, 1, 2, 3], 6, 2),
 ([2, 2, 2, 2, 2, 2, 2, 2, 0, 2], 0, 8),
 ([2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 0, 1),
 ([2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 2, 2),
 ([9,12,17,2,4,5], 17, 2)
])

def test_rotatesearch(capsys, arr, key, ind):
    with capsys.disabled():
        assert get_index(arr, key) == ind

#print(get_index([2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 2))
