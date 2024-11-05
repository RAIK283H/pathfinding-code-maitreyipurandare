import graph_data


# if n is the number, this function gets permutations for all the numbers from 1 to n-1
# so if you want to permute 5, it will give all permutations of 1-4 (i.e. 24 of them)
def SJT(n):
    nodes = list(range(1, n))

    pointing_right = [False] * (n-1)
    
    def find_largest_mobile_int(nodes):
        largest_mobile = -1
        index = -1
        for i in range (len(nodes)):
            if((pointing_right[i] == True and i < len(nodes)-1 and nodes[i] > nodes[i+1]) or (pointing_right[i] == False and i > 0 and nodes[i] > nodes[i-1])):
                if(nodes[i] > largest_mobile):
                    largest_mobile = nodes[i]
                    index = i
        return index
    
    def swap(a, b):
        nodes[a], nodes[b] = nodes[b], nodes[a]
        pointing_right[a], pointing_right[b] = pointing_right[b], pointing_right[a] 


    def switch_direction(mobile_int):
        for i in range (len(nodes)):
            if nodes[i] > mobile_int:
                pointing_right[i] = not pointing_right[i]

    
    
    permutations = [nodes[:]]

    keep_going = True
    while keep_going:
        # index of largest mobile integer in list
        mobile = find_largest_mobile_int(nodes)
        mobile_int = nodes[mobile]

        if mobile == -1:
            keep_going = False
            break
        else:
            if (pointing_right[mobile] == False):
                swap(mobile, mobile - 1)
            else:
                swap(mobile, mobile + 1)
        
        switch_direction(mobile_int)
        permutations.append(nodes[:])

    return permutations


def is_hamiltonian_cycle(permutation, graph):
    
    n = len(graph)
    if sorted(permutation) !=  list(range(1, n-1)):
        return False
    
    count = 0
    for i in range(len(permutation) - 1):
        adjacency_list = graph[permutation[i]][1]
        if (permutation[i + 1] in adjacency_list):
            count += 1
    if (permutation[0] in graph[permutation[len(permutation) - 1]][1]):
        count += 1
                
    if count == len(permutation):
        return True
    else: 
        return False

    
def get_Hamiltonian_List(permutations, graph):
    ham_cycles = []
    for permutation in permutations:
        if is_hamiltonian_cycle(permutation, graph):
            ham_cycles.append(permutation)

    if len(ham_cycles) == 0:
        return False
    else: 
        return ham_cycles

    