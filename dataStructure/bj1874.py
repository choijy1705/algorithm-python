from sys import stdin

n = int(stdin.readline().rstrip())

stack = []
k = 1
answer = []
check = True
cnt = 0
while cnt < n:
    cnt += 1
    number = int(stdin.readline().rstrip())
    while not (number in stack):
        stack.append(k)
        k += 1
        answer.append("+")
    pop = stack.pop()
    if pop != number:
        check = False
        print("NO")
        break

    answer.append("-")

if check:
    for i in range(len(answer)):
        print(answer[i])
