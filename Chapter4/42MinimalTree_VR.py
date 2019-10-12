class Node:

    def __init__(self, item):
        self.right = None
        self.left = None
        self.val = item

    def __str__(self):
        return '('+str(self.left)+':L ' + "V:" + str(self.val) + " R:" + str(self.right)+')'


def initiateArrayToBinary(array):
    return arrayToBinary(array, 0, len(array) - 1)


def arrayToBinary(array, start, end):
    if start > end:
        return None
    m = start + int((end - start)/2)
    root = Node(array[m])
    root.left = arrayToBinary(array, start, m-1)
    root.right = arrayToBinary(array, m+1, end)
    return root

testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]
print(initiateArrayToBinary(testArray))
