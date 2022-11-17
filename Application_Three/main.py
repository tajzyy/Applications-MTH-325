def is_reflexive(edge_list):
    reflexive = True
    list_one, list_two = [], []
    count = 0

    for edge in edge_list:
        node1, node2 = edge
        list_one.append(node1)
        list_two.append(node2)

    for i, j in zip(list_one, list_two):
        if i == j:
            count += 1

    nodes = [*set(list_one)]

    if nodes.__len__() != count:
        reflexive = False
        return reflexive

    return reflexive
