def is_bipartite(dictionary):
    in_nums = False
    result = True
    nums = []
    for key, value in dictionary.items():
        for i in value:
            if nums.__contains__(key):
                in_nums = True
                if nums.__contains__(i):
                    result = False
                    return result
            if not in_nums:
                nums.append(i)

    return result


true = {0: [2, 3], 1: [3, 4]}
false = {0: [1, 2, 3, 4], 1: [0, 2, 3, 4], 2: [0, 1, 3, 4], 3: [0, 1, 2, 4], 4: [0, 1, 2, 3]}
false_2 = {0: [3, 4, 5], 1: [], 2: [4], 3: [0], 4: [0, 2, 5], 5: [0, 4]}
true_2 = {0: [3, 5], 1: [4], 2: [3, 5], 3: [0, 2], 4: [1], 5: [0, 2]}

print(is_bipartite(true))
print(is_bipartite(false))
print(is_bipartite(false_2))
print(is_bipartite(true_2))
