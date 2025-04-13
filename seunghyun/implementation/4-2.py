n = int(input())
cnt = 0
currTime = [0 for _ in range(3)]

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            currTime[0], currTime[1], currTime[2] = i, j, k
            currTimeStr = ''.join(map(str, currTime))

            if '3' in currTimeStr:
                cnt += 1

print(cnt)