# 2020/11/05 (목)
# DFS/BFS-나이트의 이동
from collections import deque


def solution(size, cur_pos, dir_pos):
    chess = [[0]*size for _ in range(size)]
    return bfs(chess, cur_pos, dir_pos, size)


def bfs(chess, cur_pos, dir_pos, size):
    queue = deque()
    queue.append(cur_pos)

    # 이동할 8 방향 정의
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]

    # 큐가 빌 때까지 반복.
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= size or ny < 0 or ny >= size:
                continue
            if nx == cur_pos[0] and ny == cur_pos[1]:
                continue
            if chess[ny][nx] == 0 :
                chess[ny][nx] = chess[y][x] + 1
                queue.append((nx, ny))

    return chess[dir_pos[1]][dir_pos[0]]


if __name__ == "__main__":
    test_num = int(input())
    for _ in range(test_num):
        chess_size = int(input())   # 체스판의 크기
        cur_pos = tuple(map(int, input().split()))  # 나이트가 현재 있는 칸
        dir_pos = tuple(map(int, input().split()))  # 나이트가 이동하려고 하는 칸
        print(solution(chess_size, cur_pos, dir_pos))