from sys import stdin

K = int(stdin.readline().rstrip())

stack = []
result = 0
for _ in range(K):
    n = int(stdin.readline().rstrip())
    if n == 0:
        result -= stack.pop()
    else:
        stack.append(n)
        result += n


print(result)
