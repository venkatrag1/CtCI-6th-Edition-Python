
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isBST(root, min, max):
    if not root:
        return True
    if min and min > root.data:
        return False
    if max and max <= root.data:
        return False
    return isBST(root.left, min, root.data) and isBST(root.right, root.data, max)


# Driver Code
if __name__ == '__main__':
    root = Node(3)
    root.left = Node(2)
    root.right = Node(5)
    root.right.left = Node(1)
    root.right.right = Node(4)
    # root.right.left.left = Node(40)
    if (isBST(root ,None ,None)):
        print("Is BST")
    else:
        print("Not a BST")

        # Driver program to test above function
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)

    if (isBST(root, None, None)):
        print "Is BST"
    else:
        print "Not a BST"