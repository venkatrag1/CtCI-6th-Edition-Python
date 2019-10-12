"""
7:15

"""
from collections import deque, defaultdict

def isRectangle(mat):

    seen = defaultdict(set)

    for row in mat:
        ones = list()
        for i, col in enumerate(row):
            if col == 1:
                ones.append(i)
        for i in range(len(ones)-1):
            for j in range(i+1, len(ones)):
                if i in seen[j] or j in seen[i]:
                    return True
                seen[i].add(j)
                seen[j].add(i)
    return False




# Driver Code
if __name__ == '__main__':
    mat = [[1, 0, 0, 1, 0],
           [0, 0, 1, 0, 1],
           [0, 0, 0, 1, 0],
           [1, 0, 1, 0, 1]]
    if (isRectangle(mat)):
        print("Yes")
    else:
        print("No")

    # This code is contributed
# by SHUBHAMSINGH10