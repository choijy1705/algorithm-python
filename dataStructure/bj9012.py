n = int(input())

for _ in range(n):
    string = input()

    stack = []
    check = True
    for i in range(len(string)):
        if string[i] == "(":
            stack.append("(")
        elif string[i] == ")":
            if len(stack) < 1:
                check = False
                break
            tmp = stack.pop()
            if tmp == ")":
                check = False
                break

    if check and len(stack) == 0:
        print("YES")
    else:
        print("NO")
