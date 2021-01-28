from sys import stdin
from collections import deque

tc = int(stdin.readline().rstrip())

deque = deque()
for _ in range(tc):
    order = stdin.readline().split()

    if order[0] == "push_back":
        deque.append(order[1])
    elif order[0] == "push_front":
        deque.appendleft(order[1])
    elif order[0] == "pop_front":
        if not deque:
            print(-1)
        else:
            print(deque.popleft())
    elif order[0] == "pop_back":
        if not deque:
            print(-1)
        else:
            print(deque.pop())
    elif order[0] == "size":
        print(len(deque))
    elif order[0] == "empty":
        if not deque:
            print(1)
        else:
            print(0)
    elif order[0] == "front":
        if not deque:
            print(-1)
        else:
            print(deque[0])
    elif order[0] == "back":
        if not deque:
            print(-1)
        else:
            print(deque[len(deque) - 1])
