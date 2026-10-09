def get_user_inputs():

    heuristic = {}

    num_nodes = int(input("Enter total number of nodes: "))

    print("\nEnter heuristic value h(n) for each node:")

    for _ in range(num_nodes):
        node = input("Node name: ").strip().upper()
        h_value = float(input(f"Heuristic({node}): "))
        heuristic[node] = h_value

    graph = {node: [] for node in heuristic}

    num_edges = int(
        input("\nEnter total number of directed edges: ")
    )

    print("\nEnter edges in format:")
    print("From_Node To_Node Weight")

    for i in range(num_edges):

        u, v, w = input(
            f"Edge {i + 1}: "
        ).split()

        u = u.upper()
        v = v.upper()
        weight = float(w)

        graph[u].append((v, weight))

    return graph, heuristic


def astar(graph, heuristic, start, goal):

    open_list = [(start, 0)]

    came_from = {}

    g_cost = {start: 0}

    while open_list:

        current, current_cost = min(
            open_list,
            key=lambda x: x[1] + heuristic[x[0]]
        )

        open_list.remove((current, current_cost))

        if current == goal:

            path = [goal]

            while current in came_from:
                current = came_from[current]
                path.append(current)

            path.reverse()

            return path, g_cost[goal]

        for neighbor, cost in graph.get(current, []):

            new_cost = g_cost[current] + cost

            if (
                neighbor not in g_cost
                or new_cost < g_cost[neighbor]
            ):

                g_cost[neighbor] = new_cost
                came_from[neighbor] = current

                open_list.append(
                    (neighbor, new_cost)
                )

    return None, float("inf")


print("===== A* ALGORITHM =====")

graph, heuristic = get_user_inputs()

print("\n===== PATH FINDING =====")

start = input("Enter start node: ").strip().upper()
goal = input("Enter goal node: ").strip().upper()

path, cost = astar(
    graph,
    heuristic,
    start,
    goal
)

print("\n===== RESULT =====")

if path:
    print("Shortest path:", " -> ".join(path))
    print("Total path cost:", cost)
else:
    print("Path not found.")