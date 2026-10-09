def minimax(depth, node_index, is_max, scores, height):

    # Base case
    if depth == height:
        return scores[node_index]

    if is_max:
        return max(
            minimax(
                depth + 1,
                node_index * 2,
                False,
                scores,
                height
            ),
            minimax(
                depth + 1,
                node_index * 2 + 1,
                False,
                scores,
                height
            )
        )

    else:
        return min(
            minimax(
                depth + 1,
                node_index * 2,
                True,
                scores,
                height
            ),
            minimax(
                depth + 1,
                node_index * 2 + 1,
                True,
                scores,
                height
            )
        )


print("===== MINIMAX ALGORITHM =====")

scores = list(
    map(int, input("Enter 8 leaf node values: ").split())
)

if len(scores) != 8:
    print("Please enter exactly 8 values.")
else:
    height = 3

    result = minimax(
        0,
        0,
        True,
        scores,
        height
    )

    print("The optimal value is:", result)