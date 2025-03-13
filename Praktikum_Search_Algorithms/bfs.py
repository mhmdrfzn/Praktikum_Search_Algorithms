import collections

def bfs_path(graph, start, target):

    visited = set()
    queue = collections.deque([(start, [start])])

    while queue:
        vertex, path = queue.popleft()

        if vertex == target:
            return path
        if vertex not in visited:
            visited.add(vertex)

            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    queue.append((neighbour, path + [neighbour]))

    return "Tidak ada jalur yang ditemukan."

if __name__ == "__main__":
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}

    start_node = 2
    target_node = 3

    print(f"Berikut adalah jalur BFS dari node {start_node} ke node {target_node}:")
    print(bfs_path(graph, start_node, target_node))
