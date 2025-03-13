from queue import PriorityQueue

def greedy_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put((heuristic[start], start))  # Menyimpan (heuristik, simpul)
    explored = set()
    path = []  # Menyimpan urutan simpul yang dikunjungi

    while not frontier.empty():
        _, current_node = frontier.get()  # Ambil simpul dengan prioritas terendah

        if current_node in explored:
            continue  # Lewati jika simpul sudah dikunjungi sebelumnya

        path.append(current_node)
        explored.add(current_node)

        if current_node == goal:
            print("Simpul tujuan ditemukan!")
            print("Urutan kunjungan simpul:", " → ".join(path))
            return True

        for neighbor in graph[current_node]:
            if neighbor not in explored:
                priority = heuristic[neighbor]
                frontier.put((priority, neighbor))

    print("Simpul tujuan tidak ditemukan!")
    return False

# Heuristik (nilai estimasi ke goal)
heuristic = {
    'A': 9,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 3,
    'S': 7,
    'G': 0
}

# Graph sebagai adjacency list
graph = {
    'S': ['A', 'E'],
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['G'],
    'D': ['G'],
    'E': ['D']
}

start_node = 'S'
goal_node = 'D'

greedy_search(graph, start_node, goal_node)
