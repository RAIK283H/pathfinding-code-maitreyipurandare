import graph_data
import permutation


graph = graph_data.graph_data[1]
print(permutation.get_Hamiltonian_List((permutation.SJT(len(graph) - 1)), graph))
