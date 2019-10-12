"""
20 mins
{ {6,8}, {1,9}, {2,4}, {4,7} };
[1,9]
10:30

sort by start time; this way u keep left of smallest and then see if u need to update right
O(nlogn) to sort by start; O(n) to merge so - O(nlogn)
"""

def merge_overlapping(arr):
    if len(arr) == 0:
        return arr
    merged = []
    sorted_arr = sorted(arr, key=lambda x: x[0])
    merged.append(sorted_arr[0])
    for r in sorted_arr[1:]:
        last = merged[-1]
        if r[0] <= last[1]:
            last[0] = min(last[0], r[0])
            last[1] = max(last[1], r[1])
        else:
            merged.append(r)
    return merged
    
if __name__ == '__main__':
    input = [[6,8], [1,9], [2,4], [4,7]]
    output = [[1, 9]]
    assert merge_overlapping(input) == output

