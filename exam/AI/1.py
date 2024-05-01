def dfs(graph, start, goal):
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node == goal:
                return visited
            stack.extend(graph[node] - set(visited))
    return visited

def bfs(graph, start, goal):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            if node == goal:
                return visited
            queue.extend(graph[node] - set(visited))
    return visited

graph = {'S': set(['A', 'B', 'C']),

    'A': set(['S', 'D']),

    'B': set(['S', 'E']),

    'C': set(['S', 'F']),

    'D': set(['A']),

    'E': set(['B', 'G']),

    'F': set(['C', 'H']),

    'G': set(['E']),

    'H': set(['F'])
}


start = input("Enter the start node: ")

goal = input("Enter the goal node: ")

# Output

print("DFS: ", dfs(graph, start, goal))

print("BFS: ", bfs(graph, start, goal))