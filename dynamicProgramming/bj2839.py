N = int(input())

if N % 5 == 0:
    print(int(N / 5))

five = int(N / 5)
while ((N % 5 != 0) & (five >= 0)):
    if (N - five * 5) % 3 == 0:
        three = int((N - five * 5) / 3)
        print(five + three)
        break
    else:
        five -= 1

if five == -1:
    print(-1)
