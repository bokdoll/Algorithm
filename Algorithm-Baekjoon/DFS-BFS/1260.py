# 2020/11/06 (금)
# DFS/BFS-DFS와 BFS

from collections import defaultdict
from collections import deque


def solution():
    N, M, V = map(int, input().split()) # N: 정점의 개수, M: 간선의 개수, V: 시작할 정점의 번호
    edges = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)
    for _ in range(N):
        edges[_].sort()

    nodes = [0] * N
    return dfs(nodes, edges, V, "") + "\n" + bfs(edges, V, N)


def dfs(nodes, edges, V, answer):
    if nodes[V-1] == 0:
        nodes[V-1] = 1
        answer += str(V) + " "
        for v in edges[V]:
            answer = dfs(nodes, edges, v, answer)
        return answer
    return answer


def bfs(edges, V, N):
    nodes = [0] * N
    queue = deque()
    queue.append(V)
    nodes[V-1] = 1
    answer = str(V)

    while queue:
        x = queue.popleft()
        for v in edges[x]:
            if nodes[v-1] == 0:
                queue.append(v)
                nodes[v-1] = 1
                answer = answer + " " + str(v)
    return answer


if __name__ == "__main__":
    print(solution())