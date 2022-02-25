def solution(root, graph):
    answer = 0
    visited = []
    stack = [root]

    while stack:
        temp = stack.pop()
        if temp not in visited:
            visited.append(temp)
            tempL = sorted(graph[temp], reverse=True)
            stack.extend(tempL)
    print(visited)
    return answer


def dfs(graph, v, visited):
    visited.append(v)
    for i in graph[v]:
        if i not in visited:
            dfs(graph, i, visited)


def solution2(root, graph):
    visited = []
    dfs(graph, root, visited)
    print(visited)


if __name__ == '__main__':
    result = 0
    graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
    solution_result = solution(1, graph)
    print("Success" if result == solution_result else "Fail")
