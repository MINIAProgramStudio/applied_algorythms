import copy

def recursive_dfs(lists, memory, vertice):
    if not memory[vertice]:
        memory[vertice] = True
        selected_node = lists[vertice].first_node
        while not selected_node is None:
            memory = recursive_dfs(lists, memory, selected_node.value)
            selected_node = selected_node.next_node
    # memory[vertice] = True
    return memory

def recursive_dfs_starter(lists):
    memory = [False]*len(lists) # None for unvisited, False for pending, True for visited
    memory = recursive_dfs(lists,memory,0)
    if all(memory):
        return True
    else:
        return False

def warshall(graph):
    n = len(graph.matrix)
    w = [copy.deepcopy(graph.matrix) for i in range(n+1)]
    w[0] = graph.matrix
    for k in range(1,n+1):
        for i in range(0,n):
            for j in range(0,n):
                w[k][i][j] = w[k-1][i][j] or (w[k-1][i][k-1] and w[k-1][k-1][j])
    return w

def warshall_starter(graph):
    w = warshall(graph)
    w = w[-1]
    w = [all(row) for row in w]
    return all(w)