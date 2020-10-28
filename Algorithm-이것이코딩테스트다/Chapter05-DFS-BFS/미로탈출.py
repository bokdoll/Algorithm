# 2020/10/28 (수)
# [Chapter05-DFS/BFS 실전문제] 미로 탈출

from collections import deque


def solution():
    n, m = map(int, input().split())    # n: 세로, m: 가로
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input())))
    return bfs(graph, 0, 0, n, m)


def bfs(graph, x, y, n, m):
    queue = deque()
    queue.append((x, y))

    # 이동할 네 방향향 정의(상, 하, 좌, 우)
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # 큐가 빌 때까지 반복.
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[ny][nx] == 0:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]


if __name__ == "__main__":
    print(solution())