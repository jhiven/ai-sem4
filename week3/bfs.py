graph = {
    "40": ["10", "20"],
    "10": ["30"],
    "20": ["10", "30", "50", "60"],
    "30": ["60"],
    "50": ["70"],
    "60": ["70"],
    "70": [],
}

visited = []
queue = []


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m, end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# print("Following is the Breadth-First Search")
# bfs(visited, graph, "40")
print("Following is the Depth-First Search")
dfs(visited, graph, "40")
