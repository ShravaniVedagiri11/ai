
def alpha_beta(node, depth, alpha, beta, maximizing):

    if depth == 0:
        return node

    if maximizing:
        best = float('-inf')

        for child in node:
            value = alpha_beta(child, depth - 1, alpha, beta, False)
            best = max(best, value)
            alpha = max(alpha, best)

            if alpha >= beta:
                break

        return best

    else:
        best = float('inf')

        for child in node:
            value = alpha_beta(child, depth - 1, alpha, beta, True)
            best = min(best, value)
            beta = min(beta, best)

            if alpha >= beta:
                break

        return best


# User input
n = int(input("Enter number of groups: "))
tree = []

for i in range(n):
    values = list(map(int, input(f"Enter values for group {i+1}: ").split()))
    tree.append(values)

result = alpha_beta(tree, 2, float('-inf'), float('inf'), True)

print("Optimal value:", result)
