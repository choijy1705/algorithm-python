from sys import stdin
from queue import PriorityQueue

tc = int(stdin.readline().rstrip())

for _ in range(tc):
    N, M = map(int, stdin.readline().split())
    print_list = []

    queue = list(stdin.readline().split())
    stack = []
    k = 1
    for i in range(len(queue)):
        stack.append((queue[i], k))
        k += 1

    while len(print_list) != N:
        pop = stack.pop(0)
        tmp = []
        for i in range(len(print_list)):
            if pop[0] > print_list[i]:
                tmp.append(print_list[i])
        for i in range(len(tmp)):
            print_list.remove(tmp[i])
            stack.append(tmp[i])

        print_list.append(pop)

    print(print_list)
