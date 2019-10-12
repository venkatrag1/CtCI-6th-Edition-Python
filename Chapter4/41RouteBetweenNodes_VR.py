import Queue


class Graph(object):
    def __init__(self):
        self.vertices = []

    def addNode(self, adjacent):
        self.vertices.append(adjacent)

    def getNodes(self):
        return self.vertices


class Node(object):
    def __init__(self, vertex, adjacentLength):
        self.adjacent = []
        self.vertex = vertex
        self.visited = False

    def addAdjacent(self, node):
        self.adjacent.append(node)

    def getVertex(self):
        return self.vertex

    def getAdjacent(self):
        return self.adjacent


def createNewGraph():
    g = Graph()
    sizegraph = 6
    temp = [0] * sizegraph

    temp[0] = Node("a", 3)
    temp[1] = Node("b", 0)
    temp[2] = Node("c", 0)
    temp[3] = Node("d", 1)
    temp[4] = Node("e", 1)
    temp[5] = Node("f", 0)

    temp[0].addAdjacent(temp[1])
    temp[0].addAdjacent(temp[2])
    temp[0].addAdjacent(temp[3])
    temp[3].addAdjacent(temp[4])
    temp[4].addAdjacent(temp[5])

    for i in range(sizegraph):
        g.addNode(temp[i])
    return g


def createNewGraphWithLoop():
    g = Graph()
    temp = []

    temp.append(Node("a", 1))
    temp.append(Node("b", 1))
    temp.append(Node("c", 1))
    temp.append(Node("d", 1))
    temp.append(Node("e", 2))
    temp.append(Node("f", 0))

    temp[0].addAdjacent(temp[1])
    temp[1].addAdjacent(temp[2])
    temp[2].addAdjacent(temp[3])
    temp[3].addAdjacent(temp[4])
    temp[4].addAdjacent(temp[1])
    temp[4].addAdjacent(temp[5])

    for i in range(len(temp)):
        g.addNode(temp[i])
    return g


def breadthfirstsearch(g, start, end):
    if start == end:
        return True
    queue = Queue.Queue(len(g.getNodes()))
    start.visited = True
    print(start.getVertex())
    for adjacent in start.getAdjacent():
        queue.put(adjacent)
    while not queue.empty():
        currnode = queue.get()
        currnode.visited = True
        print(currnode.getVertex())
        if currnode.getVertex() == end.getVertex():
            return True
        for node in currnode.getAdjacent():
            if not node.visited:
                queue.put(node)
    return False

    # Create queue
    # Mark start as visited
    # Enqueue starts's children
    # while queue is not empty
        # pop node
        # visit
        # if node == one we're looking for
            # return
        # enqueue children if not visited




g = createNewGraphWithLoop()
n = g.getNodes()
start = n[0]
end = n[5]
print "Start at:", start.getVertex(), "End at: ", end.getVertex()
print breadthfirstsearch(g, start, end)
