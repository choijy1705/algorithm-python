from sys import stdin

N = int(stdin.readline().rstrip())


def sugar(N, five):
    while five >= 0:
        if N % 5 == 0:
            return int(N/5)

        sug = N - five * 5

        if sug % 3 == 0:
            return five + int(sug / 3)
        else:
            five -= 1

        if five < 0:
            return -1

print(sugar(N,int(N/5)))


