import math

def adj_list_to_matrix(graph):
    n = len(graph)
    matrix = [[math.inf] * n for _ in range(n)]
    
    for i in range(n):
        matrix[i][i] = 0
        adjacency_list = graph[i][1]
        for neighbor in adjacency_list:
            matrix[i][neighbor] = 1
    return matrix

def floyd_warshall(graph):
    distance = adj_list_to_matrix(graph)
    n = len(graph)
    parents = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph.get(i) and j in graph[i][1]:
                parents[i][j] = i
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (distance[i][k] + distance[k][j]) < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    parents[i][j] = k
    
    return distance, parents

def construct_full_path(parents, start, end):
    if parents[start][end] is None:
        return []
    
    path = [end]
    while parents[start][end] != start:
        end = parents[start][end]
        if end is None:
            return []
        path.append(end)
    path.append(start)

    return path[::-1]
    

