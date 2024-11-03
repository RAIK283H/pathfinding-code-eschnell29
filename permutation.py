
def get_all_sjt_permutations(n):
    permutations, direction = create_permutations(n)
    result = [permutations.copy()]
    
    largest, largest_index = find_largest_mobile_integer(permutations, direction, n)
    while largest_index != -1:
        swap_elements(permutations, direction, largest_index)
        reverse_direction(permutations, direction, largest)
        result.append(permutations.copy())
        largest, largest_index = find_largest_mobile_integer(permutations, direction, n)

    return result

def create_permutations(n):
    permutations = list(range(n))
    direction = [-1] * n
    return permutations, direction

def find_largest_mobile_integer(permutations, direction, n):
    largest = -1
    largest_index = -1
    for i in range(n):
        next_index = i + direction[i]
        if 0 <= next_index < n and permutations[i] > permutations[next_index]:
            if permutations[i] > largest:
                largest = permutations[i]
                largest_index = i
    return largest,largest_index

def swap_elements(permutations, direction, index):
    swap_index = index + direction[index]
    permutations[index], permutations[swap_index] = permutations[swap_index], permutations[index]
    direction[index], direction[swap_index] = direction[swap_index], direction[index]

def reverse_direction(permutations, direction, largest):
    for i in range(len(permutations)):
        if permutations[i] > largest:
            direction[i] = -direction[i]



def find_all_hamiltonian_cycles(graph):
    n = len(graph)
    sjt_perms = get_all_sjt_permutations(n)
    cycles = []

    for perm in sjt_perms:
        if is_ham_cycle(graph, perm):
            cycles.append(perm)
    
    if cycles:
        return cycles
    else:
        return -1
    
#check that the last node in the perm has the first node in its adjacency list
def is_ham_cycle(graph, path):
    if path[0] != 0 or path[-1] != len(graph) - 1:
        return False
    

    for i in range(len(path) - 1):
        current_node = path[i]
        next_node = path[i+1]
        if next_node not in graph[current_node][1]:
            return False
    
    return True
    
    