from sys import stdin

M, N = map(int, stdin.readline().split())

matrix = [[0] * M for _ in range(N)]

matrix = [list(map(int, stdin.readline().split())) for _ in range(N)]


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

cnt = 0
visited = [[0] * M for _ in range(N)]
queue = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            queue.append((i, j))

while queue:
    x, y = queue.pop(0)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0 and matrix[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                matrix[nx][ny] = matrix[x][y] + 1

max_num = 0
chk = False

for i in range(N):
    for j in range(M):
        max_num = max(max_num, int(matrix[i][j]))
        if matrix[i][j] == 0:
            chk = True
            break

if chk:
    print(-1)
else:
    print(max_num-1)
