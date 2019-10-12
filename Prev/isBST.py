
class Node:
    # constructor to create new node
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def isBSTUtil(root, min, max):
    if not root:
        return True
    if min and min > root.data:
        return False
    if max and max <= root.data:
        return False
    return isBSTUtil(root.left, min, root.data) and isBSTUtil(root.right, root.data, max)


def isbst(root):
    return isBSTUtil(root, None, None)


# driver code to test above function
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

if isbst(root):
    print("is BST")
else:
    print("not a BST")

# This code is contributed by
