import graph_data 
import global_game_data
from numpy import random
from collections import deque

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
    #preconditions
    assert global_game_data.current_graph_index < len(graph_data.graph_data)
    assert len(graph_data.graph_data[global_game_data.current_graph_index]) > 0
    
    num_nodes_visited = 0
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    start_node = 0
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    end_node = len(graph)-1

    rand_path = [start_node]
    current_node = start_node

    while current_node != target_node:
        num_nodes_visited = num_nodes_visited + 1
        neighbors = graph[current_node][1]
        next_node = int(random.choice(neighbors))
        rand_path.append(next_node)
        current_node = next_node

    while current_node != end_node:
        num_nodes_visited = num_nodes_visited + 1
        neighbors = graph[current_node][1]
        next_node = int(random.choice(neighbors))
        rand_path.append(next_node)
        current_node = next_node


    #postconditions
    assert rand_path[0] == start_node
    assert rand_path[len(rand_path) -1] == end_node
    assert target_node in rand_path
    
    return rand_path
    

def dfs_path(graph, start_node, ending_node, visited=None):
    if visited is None:
        visited = set()
    visited.add(start_node)

    if start_node == ending_node:
        return [start_node]
    
    neighbors = graph[start_node][1]
    
    for neighbor in neighbors:
        if neighbor not in visited:
            path = dfs_path(graph, neighbor, ending_node, visited)
            if path:
                return [start_node] + path
    
    return None

def get_dfs_path():
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    start_node = 0
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    end_node = len(graph)-1

    start_to_target_path = dfs_path(graph, start_node, target_node)
    if start_to_target_path is None:
        return None
    assert start_to_target_path is not None, "failed to find path to target node"
    assert target_node in start_to_target_path, "Target node isn't in path"

    target_to_exit_path = dfs_path(graph, target_node, end_node)
    if target_to_exit_path is None:
        return None
    assert target_to_exit_path is not None, "failed to find path to exit node"
    assert target_to_exit_path[-1] == end_node, "Path does not end at exit node"

    complete_path = start_to_target_path + target_to_exit_path[1:]

    for i in range(len(complete_path) - 1):
        assert complete_path[i+1] in graph[complete_path[i]][1], f" Failed: 2 Nodes are not connected"

    return complete_path

def bfs_path(graph, start_node, ending_node):
    queue = deque([(start_node, [start_node])])
    visited = set()

    while queue:
        current_node, path = queue.popleft()
        if current_node == ending_node:
            return path
        if current_node not in visited:
            visited.add(current_node)
            neighbors = graph[current_node][1]
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    
    return None

  

def get_bfs_path():
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    start_node = 0
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    end_node = len(graph)-1

    start_to_target_path = bfs_path(graph, start_node, target_node)
    assert start_to_target_path is not None, "failed to find path to target node"
    assert target_node in start_to_target_path, "Target node isn't in path"

    target_to_exit_path = bfs_path(graph, target_node, end_node)
    assert target_to_exit_path is not None, "failed to find path to exit node"
    assert target_to_exit_path[-1] == end_node, "Path does not end at exit node"

    complete_path = start_to_target_path + target_to_exit_path[1:]
    for i in range(len(complete_path) - 1):
        assert complete_path[i+1] in graph[complete_path[i]][1], f" Failed: 2 Nodes are not connected"

    return complete_path


def get_dijkstra_path():
    return [1,2]
