from sys import stdin

N, M = map(int, stdin.readline().split())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    visited = [[x, y]]
    queue = [[x, y, 1]]
    num = 999999999
    while queue:
        x, y, r = queue.pop(0)
        if x == N - 1 and y == M - 1:
            num = min(num, r)
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if [nx, ny] in visited or nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if matrix[nx][ny] == 0:
                continue
            visited.append([nx, ny])
            queue.append([nx, ny, r + 1])

    return num

matrix = [[0] * M for _ in range(N)]

for i in range(N):
    string = stdin.readline().rstrip()
    for j in range(M):
        matrix[i][j] = int(string[j])

print(bfs(0, 0))



