from sys import stdin
from collections import deque

N = int(stdin.readline().rstrip())
queue = deque()

for i in range(N):
    queue.append(i+1)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue.pop())