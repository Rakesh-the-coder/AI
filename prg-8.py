from collections import deque


def water_jug(capacity1, capacity2, target):

    visited = set()

    queue = deque()

    # Initial state
    queue.append((0, 0, []))

    while queue:

        jug1, jug2, path = queue.popleft()

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        current_path = path + [(jug1, jug2)]

        # Goal check
        if jug1 == target or jug2 == target:
            return current_path

        # Possible operations

        next_moves = [

            # Fill jug 1
            (capacity1, jug2),

            # Fill jug 2
            (jug1, capacity2),

            # Empty jug 1
            (0, jug2),

            # Empty jug 2
            (jug1, 0),

            # Pour jug 1 -> jug 2
            (
                jug1 - min(jug1, capacity2 - jug2),
                jug2 + min(jug1, capacity2 - jug2)
            ),

            # Pour jug 2 -> jug 1
            (
                jug1 + min(jug2, capacity1 - jug1),
                jug2 - min(jug2, capacity1 - jug1)
            )
        ]

        for move in next_moves:

            if move not in visited:
                queue.append(
                    (move[0], move[1], current_path)
                )

    return None


capacity1 = int(input("Enter capacity of jug 1: "))
capacity2 = int(input("Enter capacity of jug 2: "))
target = int(input("Enter target amount: "))

solution = water_jug(
    capacity1,
    capacity2,
    target
)

if solution:

    print("\nSteps to reach target:")

    for step in solution:
        print(step)

else:
    print("No solution exists.")