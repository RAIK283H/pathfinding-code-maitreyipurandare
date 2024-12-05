import graph_data
import math
import global_game_data


def weight(u, v, graph):
    x1, y1 = graph[u][0]
    x2, y2 = graph[v][0]
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


def graph_data_to_matrix(graph):
    matrix = [[float('inf') for _ in range(len(graph))] for _ in range(len(graph))]

    for vertex, (coordinates, neighbors) in enumerate (graph):
        matrix[vertex][vertex] = 0
        for neighbor in neighbors:
            matrix[vertex][neighbor] = weight(vertex, neighbor, graph)
    return matrix

def build_path(parent, start, end):
    if parent[start][end] == -1:
        return []
    path = [end]
    while start != end:
        end = parent[start][end]
        path.append(end)

    path.reverse()
    return path 


def floyd_warshall():
    graph = graph_data.graph_data[global_game_data.current_graph_index] 
    matrix = graph_data_to_matrix(graph)

    parent = []
    for row in range (len(matrix)):
        row_list = []
        for col in range (len(matrix)):
            if matrix[row][col] == float('inf'):
                row_list.append(-1)
            else:
                row_list.append(row)
        parent.append(row_list)

    for k in range(len(matrix)):
        for i in range (len(matrix)):
            for j in range (len(matrix)):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
                    parent[i][j] = parent[k][j]
    start_node = 0
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    path = build_path(parent, start_node, target_node)
    exit_node = len(graph) - 1
    path2 = build_path(parent, target_node, exit_node)
    path2.pop(0)
    global_game_data.fw_counter = len(path + path2) - 1
    return path+path2





