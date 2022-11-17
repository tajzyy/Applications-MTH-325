def is_reflexive(edge_list):
    reflexive = True
    list_one, list_two = [], []
    count = 0

    for edge in edge_list:
        node1, node2 = edge
        list_one.append(node1)
        list_two.append(node2)

    for i in list_one:
        for j in list_two:
            if i == j:
                count += 1

    nodes = [*set(list_one)]

    if nodes.__len__() != count:
        reflexive = False
        return reflexive

    return reflexive




print(is_reflexive([(1, 1), (2, 2), (3, 3)]))
