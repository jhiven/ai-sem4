graph = {
    "0": {"3": 8, "4": 4},
    "1": {"0": 2, "6": 11},
    "2": {"5": 1, "6": 1},
    "3": {"1": 6, "7": 9},
    "4": {"6": 5},
    "5": {"6": 2, "7": 2},
    "6": {"2": 4, "4": 5},
    "7": {"5": 3},
}

visited_bfs = []
queue_bfs = []
visited_dfs = []

def bfs(visited, graph, node):
    visited.append(node)
    queue_bfs.append(node)
    while queue_bfs:
        m = queue_bfs.pop(0)
        print(m, end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue_bfs.append(neighbour)


def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


print("Following is the Breadth-First Search")
bfs(visited_bfs, graph, "0")
print("")
print("Following is the Depth-First Search")
dfs(visited_dfs, graph, "0")
