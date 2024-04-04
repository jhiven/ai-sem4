graph = {
    "A": ["B", "C"],
    "B": ["H"],
    "C": ["D", "E"],
    "D": ["F", "G"],
    "F": ["H"],
    "G": ["I"],
    "H": ["I"],
    "E": ["I"],
    "I": [],
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
bfs(visited_bfs, graph, "A")
print("")
print("Following is the Depth-First Search")
dfs(visited_dfs, graph, "A")
