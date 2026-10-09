def alpha_beta(
    depth,
    node_index,
    maximizing_player,
    values,
    alpha,
    beta,
    height
):

    # Base case
    if depth == height:
        return values[node_index]

    if maximizing_player:

        best = float("-inf")

        best = max(
            best,
            alpha_beta(
                depth + 1,
                node_index * 2,
                False,
                values,
                alpha,
                beta,
                height
            )
        )

        alpha = max(alpha, best)

        if beta <= alpha:
            return best

        best = max(
            best,
            alpha_beta(
                depth + 1,
                node_index * 2 + 1,
                False,
                values,
                alpha,
                beta,
                height
            )
        )

        return best

    else:

        best = float("inf")

        best = min(
            best,
            alpha_beta(
                depth + 1,
                node_index * 2,
                True,
                values,
                alpha,
                beta,
                height
            )
        )

        beta = min(beta, best)

        if beta <= alpha:
            return best

        best = min(
            best,
            alpha_beta(
                depth + 1,
                node_index * 2 + 1,
                True,
                values,
                alpha,
                beta,
                height
            )
        )

        return best


print("===== ALPHA-BETA PRUNING =====")

values = list(
    map(int, input("Enter 8 leaf node values: ").split())
)

if len(values) != 8:
    print("Please enter exactly 8 values.")
else:

    height = 3

    alpha = float("-inf")
    beta = float("inf")

    result = alpha_beta(
        0,
        0,
        True,
        values,
        alpha,
        beta,
        height
    )

    print("Optimal value:", result)