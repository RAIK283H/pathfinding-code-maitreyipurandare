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

        path.append(int(next_node))
        current_node = next_node
        global_game_data.counter += 1

    while(current_node != end_node):
        adjacency_list = graph_data.graph_data[global_game_data.current_graph_index][current_node][1]
       
        next_node = random.choice(adjacency_list)

        path.append(int(next_node))
        current_node = next_node
        global_game_data.counter += 1
        

    assert len(path) > 0, "path was not created correctly"
    return path


def get_dfs_path():
    path = []
    end_node = len(graph_data.graph_data[global_game_data.current_graph_index]) - 1

    target = global_game_data.target_node[global_game_data.current_graph_index]
    frontier = []
    frontier.append(0)

    visited = set()
    visited.add(0)

    parents = {}
    parents[0] = False

    while frontier:
        current = frontier.pop()
        if current == target:
            path.append(current)
            break

        neighbors = graph_data.graph_data[global_game_data.current_graph_index][current][1]

        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = current
                frontier.append(neighbor)

    while current:
        current = parents[current]
        path.insert(0, current)

    # target to end node
    visited.clear()
    frontier = [target]

    while frontier:
        current = frontier.pop()
        if current == end_node:
            # path.append(current)
            break

        neighbors = graph_data.graph_data[global_game_data.current_graph_index][current][1]

        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = current
                frontier.append(neighbor)

    path2 = []
    while current != False and current != target:
        path2.insert(0, current)
        current = parents[current]
    
    global_game_data.dfs_counter = len(path + path2)
    for i in range (len(path) - 1):
        assert path[i + 1] in graph_data.graph_data[global_game_data.current_graph_index][path[i]][1], "not every pair of sequential vertices in the path is connected by an edge"

    assert target in path, "target node is not in path" 
    assert path2[len(path2) - 1] == end_node, "path does not exit at end node"
    return path + path2

    
def get_bfs_path():
    path = []
    end_node = len(graph_data.graph_data[global_game_data.current_graph_index]) - 1

    target = global_game_data.target_node[global_game_data.current_graph_index]
    frontier = []
    frontier.append(0)

    visited = set()
    visited.add(0)

    parents = {}
    parents[0] = False

    while frontier:
        current = frontier.pop(0)
        if current == target:
            path.append(current)
            break

        neighbors = graph_data.graph_data[global_game_data.current_graph_index][current][1]

        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = current
                frontier.append(neighbor)

    while current:
        current = parents[current]
        path.insert(0, current)

    # target to end node
    visited.clear()
    frontier = [target]

    while frontier:
        current = frontier.pop(0)
        if current == end_node:
            # path.append(current)
            break

        neighbors = graph_data.graph_data[global_game_data.current_graph_index][current][1]

        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = current
                frontier.append(neighbor)

    path2 = []
    while current != False and current != target:
        path2.insert(0, current)
        current = parents[current]
    
    global_game_data.bfs_counter = len(path + path2)
    for i in range (len(path) - 1):
        assert path[i + 1] in graph_data.graph_data[global_game_data.current_graph_index][path[i]][1], "not every pair of sequential vertices in the path is connected by an edge"

    assert target in path, "target node is not in path" 
    assert path2[len(path2) - 1] == end_node, "path does not exit at end node"
        
    return path + path2


def get_dijkstra_path():
    return [1,2]
