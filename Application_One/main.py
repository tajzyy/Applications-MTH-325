def is_bipartite(dictionary):
    in_b = False
    result = True
    group_a = []
    group_b = []
    for key, value in dictionary.items():
        for i in value:
            if group_b.__contains__(key):
                in_b = True
                if not group_b.__contains__(i) and not group_a.__contains__(key):
                    group_b.append(i)
                elif group_b.__contains__(i):
                    result = False
                    return result
            if not in_b:
                group_a.append(i)
                group_b.append(i)

    return result


true = {0: [2, 3], 1: [3, 4]}
false = {0: [1, 2, 3, 4], 1: [0, 2, 3, 4], 2: [0, 1, 3, 4], 3: [0, 1, 2, 4], 4: [0, 1, 2, 3]}
false_2 = {0: [3, 4, 5], 1: [], 2: [4], 3: [0], 4: [0, 2, 5], 5: [0, 4]}
true_2 = {0: [3, 5], 1: [4], 2: [3, 5], 3: [0, 2], 4: [1], 5: [0, 2]}

print(is_bipartite(true))
print(is_bipartite(false))
print(is_bipartite(false_2))
print(is_bipartite(true_2))