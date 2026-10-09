def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        current = queue.pop(0)

        if current not in visited:
            print("Exploring node:", current)
            visited.append(current)

            for neighbor in graph.get(current, []):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

    return visited


print("===== BREADTH FIRST SEARCH =====")

graph = {}

num_edges = int(input("Enter number of edges: "))

print("Enter each edge (example: A B):")

for i in range(num_edges):
    u, v = input(f"Edge {i + 1}: ").split()

    if u not in graph:
        graph[u] = []

    if v not in graph:
        graph[v] = []

    graph[u].append(v)
    graph[v].append(u)

start = input("Enter starting node: ")

print("\nGraph:", graph)
print("\nBFS Traversal:")

bfs(graph, start)