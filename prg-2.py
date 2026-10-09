def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        current = stack.pop()

        if current not in visited:
            print("Exploring node:", current)
            visited.append(current)

            for neighbor in reversed(graph.get(current, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited


print("===== DEPTH FIRST SEARCH =====")

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
print("\nDFS Traversal:")

dfs(graph, start)