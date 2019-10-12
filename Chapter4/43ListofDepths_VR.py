from collections import deque

class newnode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.nextRight = None


def connect_preorder(root): # preorder way - works for complete binary tree; level order if not
    if not root:
        return
    if root.left:
        root.left.nextRight = root.right
    if root.right:
        if root.nextRight:
            root.right.nextRight = root.nextRight.left
    connect(root.left)
    connect(root.right)


def connect_BFS(root):
    queue = deque()
    queue.append(root)
    queue.append(None)
    while len(queue) > 0:
        current = queue.popleft()
        if current:
            current.nextRight = queue[0]
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        elif len(queue) > 0:
                queue.append(None)


# Driver Code
if __name__ == '__main__':

    # Constructed binary tree is
    #         10
    #     / \
    #     8     2
    # /
    # 3
    root = newnode(10)
    root.left = newnode(8)
    root.right = newnode(2)
    root.left.left = newnode(3)

    # Populates nextRight pointer in all nodes
    #connect = connect_preorder
    connect = connect_BFS
    connect(root)

    # Let us check the values of nextRight pointers
    print("Following are populated nextRight",
          "pointers in the tree (-1 is printed",
          "if there is no nextRight)")
    print("nextRight of", root.data, "is "),
    if root.nextRight:
        print(root.nextRight.data)
    else:
        print(-1)
    print("nextRight of", root.left.data, "is "),
    if root.left.nextRight:
        print(root.left.nextRight.data)
    else:
        print(-1)
    print("nextRight of", root.right.data, "is "),
    if root.right.nextRight:
        print(root.right.nextRight.data)
    else:
        print(-1)
    print("nextRight of", root.left.left.data, "is "),
    if root.left.left.nextRight:
        print(root.left.left.nextRight.data)
    else:
        print(-1)

        # This code is contributed by PranchalK