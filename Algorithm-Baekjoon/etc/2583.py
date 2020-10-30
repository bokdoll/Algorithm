# 2020/10/30 (금)
# DFS/BFS-영역 구하기
from collections import deque


def solution():
    # 그래프 그리기
    m, n, k = map(int, input().split())  # m : 세로, n: 가로, k: 직사각형 개수
    graph = [[0] * n for _ in range(m)]
    for _ in range(k):
        a, b, c, d = map(int, input().split())
        if b > d:
            temp = b
            b = d
            d = temp
        if a > c:
            temp = a
            a = c
            c = temp
        for j in range(b, d):
            for i in range(a, c):
                graph[j][i] = 1

    result = []
    for j in range(m):
        for i in range(n):
            if graph[j][i] == 0:
                size = bfs(graph, i, j, m, n, 0)
                if size == 0:
                    size = 1
                result.append(size)
    print(len(result))
    return ' '.join(list(map(str, sorted(result))))


def bfs(graph, x, y, m, n, size):
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

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[ny][nx] == 1:
                continue
            if graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                queue.append((nx, ny))
                size += 1
    return size


if __name__ == "__main__":
    print(solution())