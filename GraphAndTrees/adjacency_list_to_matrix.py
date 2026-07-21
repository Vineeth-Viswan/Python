def adjacency_list_to_matrix(adjacency_list):
    nodes = list(adjacency_list.keys())

    for neighbors in adjacency_list.values():
        for node in neighbors:
            if node not in adjacency_list and node not in nodes:
                nodes.append(node)

    node_to_index = {node: index for index, node in enumerate(nodes)}
    size = len(nodes)
    matrix = [[0 for _ in range(size)] for _ in range(size)]

    for node, neighbors in adjacency_list.items():
        row_index = node_to_index[node]
        for neighbor in neighbors:
            matrix[row_index][node_to_index[neighbor]] = 1

    for row in matrix:
        print(row)

    return matrix