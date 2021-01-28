from sys import stdin

N, K = map(int, stdin.readline().split())

queue = [i for i in range(1,N+1)]

index = K-1
print("<", end = "")
while len(queue)>0:
    print(queue.pop(index), end = "")
    if queue:
        print(", ",end = "")
    else:
        break
    index += K-1
    while index > len(queue)-1:
        index -= len(queue)

print(">",end = "")
