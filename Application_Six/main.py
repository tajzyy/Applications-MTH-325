def maximal_elements(edge_list):
    maximals = []
    count = 0

    for edge in edge_list:
        for i in edge_list:
            if i % edge == 0:
                count += 1
        if count == 1:
            maximals.append(edge)
            count = 0
        else:
            count = 0

    return maximals


def greatest_element(edge_list):
    greatest = maximal_elements(edge_list)
    
    if greatest.__len__() > 1
        greatest.clear
        
    return greatest


print(maximal_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 24]))
print(greatest_element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 24]))
print(greatest_element([2, 4, 8, 16, 32]))
