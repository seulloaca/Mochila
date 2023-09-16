capacidad = 8
P = [7, 4, 4]
V = [50, 26, 26]

memo = [[0] * capacidad for _ in range(len(V))]


def knapsack(item, cap):
    if cap < 0:
        return (1 << 60) * -1
    if item == -1:
        return 0
    if cap == 0:
        return 0
    if memo[item][cap - 1]:
        return memo[item][cap - 1]

    memo[item][cap - 1] = max(knapsack(item - 1, cap), V[item] + knapsack(item - 1, cap - P[item]))
    return memo[item][cap - 1]


print('Valor máximo ' + str(knapsack(len(V) - 1, capacidad)))
