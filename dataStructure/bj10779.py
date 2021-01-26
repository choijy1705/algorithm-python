from sys import stdin

string = stdin.readline().rstrip()

cnt = 0
bar = 0
result = 0
stack = []
laser = False
for i in range(len(string)-1):
    if string[i] == "(" and string[i+1] == ")":
        continue
    elif string[i] == "(":
        bar += 1
    elif string[i] == ")" and string[i-1] == "(":
        result += bar
    elif string[i] == ")":
        result += 1
        bar -= 1

result += bar

print(result)
