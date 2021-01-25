from sys import stdin

N, K = map(int, stdin.readline().split())

list = []
for i in range(N):
    list.append(i+1)

index = 0
print("<", end="")
while(len(list) > 0):
    index += K-1
    while index > len(list) - 1:
        index -= len(list)

    print(list.pop(index), end="")
    if len(list) != 0:
        print(", ", end="")

print(">")

