def maximal_elements(edge_list):
    maximals = []
    list_one, list_two = [], []
    count = 0

    for edge in edge_list:
        node1, node2 = edge
        list_one.append(node1)
        list_two.append(node2)

    for i, j in zip(list_one, list_two):
        if (not list_one.count(i) > 1) and (i == j):
            maximals.append(i)
        elif not list_one.__contains__(j):
            maximals.append(j)

    maximals = [*set(maximals)]

    return maximals


def greatest_element(edge_list):
    greatest = maximal_elements(edge_list)

    if greatest.__len__() > 1:
        greatest.clear()

    return greatest


print(maximal_elements([(0, 1), (0, 2), (1, 2), (2, 3), (3, 1)]))
print(maximal_elements([(0, 3), (1, 2), (1, 3)]))
print(greatest_element([(0, 1), (1, 2)]))
