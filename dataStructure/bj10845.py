from sys import stdin



def push(x):
    queue.append(x)

def pop():
    return queue.pop(0) if len(queue) > 0 else -1

def size():
    return len(queue)

def empty():
    return 0 if len(queue) > 0 else 1

def front():
    return queue[0] if len(queue) > 0 else -1

def back():
    return queue[len(queue)-1] if len(queue) > 0 else -1

n = int(stdin.readline().rstrip())

queue = []

for _ in range(n):
    input_split = stdin.readline().rstrip().split()

    order = input_split[0]

    if order == "push":
        push(input_split[1])
    elif order == "pop":
        print(pop())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    elif order == "front":
        print(front())
    elif order == "back":
        print(back())