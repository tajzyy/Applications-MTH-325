def maximal_elements(edge_list):
    maximals = []
    list_one, list_two = [], []
    count = 0

    for edge in edge_list:
        node1, node2 = edge
        list_one.append(node1)
        list_two.append(node2)

    for i in list_one:
        if not list_one.count(i) > 1:
            maximals.append(i)

    maximals = [*set(maximals)]

    return maximals


def greatest_element(edge_list):
    greatest = maximal_elements(edge_list)
    
    if greatest.__len__() > 1:
        greatest.clear()
        
    return greatest

