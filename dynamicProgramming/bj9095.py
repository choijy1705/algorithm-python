n = int(input())

for i in range(n):
    num = int(input())

    dp = {0: 0, 1: 1, 2: 2, 3: 4}

    if num <= 3:
        print(dp[num])
    else:
        for i in range(4,num+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        print(dp[num])

