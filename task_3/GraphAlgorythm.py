def recursive_dfs(lists, memory, vertice):
    if memory[vertice] is None:
        memory[vertice] = False
        selected_node = lists[vertice].first_node
        while not selected_node is None:
            memory = recursive_dfs(lists, memory, selected_node.value)
            selected_node = selected_node.next_node
    memory[vertice] = True
    return memory

def recursive_dfs_starter(lists):
    memory = [None]*len(lists)
    memory = recursive_dfs(lists,memory,0)
    if all(memory):
        return True
    else:
        return False




