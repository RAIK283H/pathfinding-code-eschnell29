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
    



def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
