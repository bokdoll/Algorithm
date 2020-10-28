# 2020/10/28 (수)
# [Chapter05-DFS/BFS 실전문제] 음료수 얼려 먹기

def solution():
    n, m = map(int, input().split())    # n: 세로, m: 가로
    graph = []
    for i in range(n):
        graph.append(list(map(int, input())))

    # 모든 노드(위치)에 대하여 음료수 채우기
    result = 0
    for i in range(m):
        for j in range(n):
            # 현재 위치에서 DFS 수행
            if dfs(graph, i, j, n, m):
                result += 1

    return result


# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(graph, x, y, n, m):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if graph[y][x] == 0:
        graph[y][x] = 1
        dfs(graph, x - 1, y, n, m)
        dfs(graph, x, y - 1, n, m)
        dfs(graph, x + 1, y, n, m)
        dfs(graph, x, y + 1, n, m)
        return True
    return False


if __name__ == "__main__":
    print(solution())