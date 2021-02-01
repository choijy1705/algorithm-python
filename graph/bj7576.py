from sys import stdin
from collections import deque


def bfs(M, N, box):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    days = -1

    while queue:
        days += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                    box[nx][ny] = box[x][y] + 1
                    queue.append([nx, ny])

    for b in box:
        if 0 in b:
            return -1
    return days


M, N = map(int, stdin.readline().split())
box = []
queue = deque()
for i in range(N):
    row = list(map(int, stdin.readline().split()))
    for j in range(M):
        if row[j] == 1:
            queue.append([i, j])
    box.append(row)

print(bfs(M, N, box))
