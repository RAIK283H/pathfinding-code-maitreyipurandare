import graph_data
import global_game_data
from numpy import random
import heapq
import Node
import math
import f_w

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    #global_game_data.graph_paths.append(get_dijkstra_path())
    global_game_data.graph_paths.append(f_w.floyd_warshall())



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
        #assert current in graph_data.graph_data[global_game_data.current_graph_index][target][1], "Not an adjacent move!"
        
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
    global_game_data.dfs_counter = len(path + path2) - 1
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
    
    global_game_data.bfs_counter = len(path + path2) - 1
    for i in range (len(path) - 1):
        assert path[i + 1] in graph_data.graph_data[global_game_data.current_graph_index][path[i]][1], "not every pair of sequential vertices in the path is connected by an edge"

    assert target in path, "target node is not in path" 
    assert path2[len(path2) - 1] == end_node, "path does not exit at end node"
        
    return path + path2


def get_dijkstra_path():
    path1 = []
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    start = 0
    end = len(graph) - 1
    target = global_game_data.target_node[global_game_data.current_graph_index]

    priority_queue = []
    heapq.heappush(priority_queue, Node.Node(start, 0))
    distances = {start: 0}
    parents = {start: None}
    visited = set()

    while priority_queue:
        current = heapq.heappop(priority_queue)
        current_index = current.index

        if current_index not in visited:
            visited.add(current_index)
        else:
            continue

        if current_index == target:
            break

        neighbors = graph[current_index][1]

        for neighbor in neighbors:
            cost = getDistance(current_index, neighbor, graph)
            new_dist = distances[current_index] + cost

            if neighbor not in visited: 
                distances[neighbor] = new_dist
                parents[neighbor] = current_index
                heapq.heappush(priority_queue, Node.Node(neighbor, new_dist))

    current_index = target
    while current_index is not None:
        path1.insert(0, current_index)
        current_index = parents.get(current_index)

    priority_queue = []
    heapq.heappush(priority_queue, Node.Node(target, 0))
    distances = {target: 0}
    parents = {target: None}
    visited = set()

    while priority_queue:
        current = heapq.heappop(priority_queue)
        current_index = current.index

        if current_index not in visited:
            visited.add(current_index)
        else:
            continue

        if current_index == end:
            break

        neighbors = graph[current_index][1]

        for neighbor in neighbors:
            cost = getDistance(current_index, neighbor, graph)
            new_dist = distances[current_index] + cost

            if neighbor not in visited: 
                distances[neighbor] = new_dist
                parents[neighbor] = current_index
                heapq.heappush(priority_queue, Node.Node(neighbor, new_dist))

    path2 = []
    current_index = end
    while current_index is not None and current_index != target:
        path2.insert(0, current_index)
        current_index = parents.get(current_index)
        
    
    path = path1 + path2
    for i in range (len(path) - 1):
        assert path[i + 1] in graph[path[i]][1], "not every pair of sequential vertices in the path is connected by an edge"

    assert target in path, "target node is not in path" 
    assert path[0] == start, "path does not start at start node"
    assert path[len(path) - 1] == end, "path does not exit at end node"
    global_game_data.dijkstra_counter = len(path)
    return path

def getDistance(node1, node2, graph):
    x1, y1 = graph[node1][0]
    x2, y2 = graph[node2][0]
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)