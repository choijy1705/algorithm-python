from sys import stdin

N = int(stdin.readline().rstrip())
M = int(stdin.readline().rstrip())

matrix = [[0] * (N+1) for _ in range(N+1)]
visit = [0] * (N+1)

for _ in range(M):
    a,b = map(int,stdin.readline().split())

    matrix[a][b] = 1
    matrix[b][a] = 1

queue = []
queue.append(1)
visit[1] = 1
cnt = 0
while queue:
    com = queue.pop(0)

    for i in range(len(matrix[com])):
        if matrix[com][i] == 1 and visit[i] == 0:
            visit[i] = 1
            queue.append(i)
            cnt += 1

print(cnt)