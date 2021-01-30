from sys import stdin

N = int(stdin.readline().rstrip())
matrix = [stdin.readline().rstrip() for _ in range(N)]
visited = [[0] * N for _ in range(N)]
apart = []
count_apart = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y):
    queue = [(x, y)]
    visited[x][y] = 1
    cnt = 1
    while queue:
        x, y = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N:
                if visited[nx][ny] == 0:
                    if matrix[nx][ny] == '1':
                        visited[nx][ny] = 1
                        queue.append((nx,ny))
                        cnt += 1
    apart.append(cnt)


for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and matrix[i][j] == '1':
            count_apart += 1
            bfs(i, j)

apart.sort()

print(count_apart)
for result in apart:
    print(result)
