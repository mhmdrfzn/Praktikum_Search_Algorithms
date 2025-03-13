from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited, path, target):
        visited.add(v)
        path.append(v)

        if v == target:
            return True

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                if self.DFSUtil(neighbour, visited, path, target):
                    return True

        path.pop()
        return False

    def findPathDFS(self, start, target):
        visited = set()
        path = []

        if self.DFSUtil(start, visited, path, target):
            return path
        else:
            return "Tidak ada jalur yang ditemukan."

if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    start_node = 1
    target_node = 3

    print(f"Berikut adalah jalur DFS dari node {start_node} ke node {target_node}:")
    print(g.findPathDFS(start_node, target_node))
