from collections import deque


def solution(root, graph):
    answer = 0
    queue = deque([root])
    visited = []
    while queue:
        temp = queue.popleft()
        if temp not in visited:
            visited.append(temp)
            for i in graph[temp]:
                if i not in visited:
                    queue.append(i)

    print(visited)
    return answer


if __name__ == '__main__':
    result = 0
    graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
    solution_result = solution(1, graph)
    print("Success" if result == solution_result else "Fail")
