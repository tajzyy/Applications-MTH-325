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


def is_symmetric(edge_list):
    symmetric = True
    list_one, list_two = [], []
    node_list1, node_list2 = [], []

    for edge in edge_list:
        node1, node2 = edge
        list_one.append(node1)
        list_two.append(node2)

    for i, j in zip(list_one, list_two):
        if i != j:
            node_list1.append(i)
            node_list2.append(j)

    node_list1.sort()
    node_list2.sort()

    if node_list1 != node_list2:
        symmetric = False
        return symmetric

    return symmetric


def is_transitive(edge_list):
    transitive = True
    list_one, list_two = [], []
    node_list1, node_list2, node_list3 = [], [], []

    for edge in edge_list:
        node1, node2 = edge
        list_one.append(node1)
        list_two.append(node2)

    for i, j in zip(list_one, list_two):
        if i != j and not node_list2.__contains__(i):
            node_list2.append(j)
        if node_list2.__contains__(i):
            node_list3.append(j)
            count += 1

    node_list3 = [*set(node_list3)]
    
    if node_list2 != node_list3:
        transitive = False
        return transitive

    return transitive
