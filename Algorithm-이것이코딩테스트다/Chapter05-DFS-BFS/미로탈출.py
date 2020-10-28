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

    # 이동할 네 방향향 정의(하, 우, 상, 좌)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    answer = 1

    # 큐가 빌 때까지 반봅
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == m-1 and ny == n-1:
                return answer + 1
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            elif graph[ny][nx] == 1:
                print(nx, ny)
                answer += 1
                queue.append((nx, ny))
                graph[ny][nx] = 0
                break
            else:
                continue
    return answer


if __name__ == "__main__":
    print(solution())