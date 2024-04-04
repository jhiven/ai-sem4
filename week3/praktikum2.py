graph = {
    "1": {"2": 1, "3": 2},
    "2": {"4": 6, "5": 12},
    "3": {"4": 3, "6": 4},
    "4": {"5": 4, "6": 3, "7": 15, "8": 7},
    "5": {"7": 7},
    "6": {"8": 7, "9": 15},
    "7": {"9": 9},
    "8": {"9": 10},
    "9": {},
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
bfs(visited_bfs, graph, "1")
print("")
print("Following is the Depth-First Search")
dfs(visited_dfs, graph, "1")
