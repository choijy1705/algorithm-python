from sys import stdin

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def move(x,y,t,r):
    global ans,dir,head,tail
    for i in range(t):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if not 0 <= nx < N or not 0 <= ny < N:
            return 1
        if snake[nx][ny]:
            return 1

        snake[nx][ny] = snake[x][y] + 1
        head = [nx,ny]
        if apple[nx][ny] == 1:
            apple[nx][ny] = 0
        else:
            tx, ty = tail
            for j in range(4):
                ntx = tx + dx[j]
                nty = ty + dy[j]
                if not 0 <= ntx < N or not 0 <=nty < N:
                    continue
                if snake[ntx][nty] - snake[tx][ty] == 1:
                    snake[tx][ty] = 0
                    tail = [ntx,nty]
                    break
        x,y = nx, ny
        ans += 1
    dir = (dir + 1) % 4 if r == 'D' else (dir + 3) % 4

N = int(stdin.readline().rstrip())
K = int(stdin.readline().rstrip())
apple = [[0] * N for _ in range(N)]

for i in range(K):
    x, y = map(int, stdin.readline().split())
    apple[x-1][y-1] = 1

rotate =[]
L = int(stdin.readline().rstrip())

for _ in range(L):
    x, c = list(stdin.readline().split())
    rotate.append([x,c])

bt, ans, dir, flag = 0, 0, 0, 0
snake = [[0] * N for _ in range(N)]
snake[0][0] = 1
head, tail = [0,0], [0,0]
for t,r in rotate:
    nt = int(t) - bt
    res = move(head[0], head[1], nt, r)
    if res:
        print(ans+1)
        flag = 1
        break
    bt = int(t)

if flag == 0:
    move(head[0], head[1], N, r)
    print(ans+1)

