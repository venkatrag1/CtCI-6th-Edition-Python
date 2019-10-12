from collections import defaultdict
from collections import deque

class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, start, end):
        if start == end:
            return True
        visited = [False] * len(self.graph)
        visited[start] = True
        q = deque()
        for node in self.graph[start]:
            if not visited[node]:
                q.append(node)
        while len(q) > 0:
            currnode = q.popleft()
            visited[currnode] = True
            print(currnode)
            if currnode == end:
                return True
            for node in self.graph[currnode]:
                if not visited[node]:
                    q.append(node)
        return False








g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print ("Following is Breadth First Traversal"
       " (starting from vertex 2)")
g.BFS(2, 1)


