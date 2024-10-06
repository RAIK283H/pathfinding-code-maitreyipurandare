import graph_data
import global_game_data
from numpy import random

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]



def get_random_path():

    # precondition
    assert graph_data.graph_data[global_game_data.current_graph_index] is not None, "this graph is null"
    assert  len(graph_data.graph_data[global_game_data.current_graph_index]) >= 2, "this graph does not have enough nodes"
    
    start_node = 0
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    path = [start_node]
    current_node = start_node
    end_node = len(graph_data.graph_data[global_game_data.current_graph_index]) - 1

    while(current_node != target_node):
        adjacency_list = graph_data.graph_data[global_game_data.current_graph_index][current_node][1]
       
        next_node = random.choice(adjacency_list)

        path.append(next_node)
        current_node = next_node
        global_game_data.counter += 1

    while(current_node != end_node):
        adjacency_list = graph_data.graph_data[global_game_data.current_graph_index][current_node][1]
       
        next_node = random.choice(adjacency_list)

        path.append(next_node)
        current_node = next_node
        global_game_data.counter += 1


    assert len(path) > 0, "path was not created correctly"
    return path


def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
