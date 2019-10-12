
"""
Input: arr[] = {7, 10, 4, 3, 20, 15}
       k = 3
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15}
       k = 4

       9:15 - sort and traverse O(NlogN)
       can u do in O(N) - max heap or max heap -   7, 10, 20 -   4, 3, 15
       9:24

"""


class MinHeap(object):
    def __init__(self):
        self.heap = []

    def extract_min(self):
        pass

    def heapify(self):
        pass


def find_k_smallest(arr, k):
