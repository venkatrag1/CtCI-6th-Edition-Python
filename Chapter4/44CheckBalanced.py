"""
10.00
balanced if left balanced and right balanced
base case

"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def treeHeight(root):
    if root == None:
        return 0
    lh = treeHeight(root.left)
    if lh == -1:
        return -1
    rh = treeHeight(root.right)
    if rh == -1:
        return -1
    if abs(lh - rh) > 1:
        return -1
    else:
        return 1 + max(lh, rh)


def isBalanced(root):
    return treeHeight(root) != -1



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.left.left.left = Node(7)

if isBalanced(root):
    print('Tree is balanced')
else:
    print('Tree is not balanced')

# Driver function to test the above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)
if isBalanced(root):
    print("Tree is balanced")
else:
    print("Tree is not balanced")