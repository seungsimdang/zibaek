pos = input()

x = pos[0]
y = int(pos[1])

alphabet = "abcdefghijklmnopqrstuzwxyz"
x_idx = alphabet.index(x) + 1

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

cnt = 0

for i in range(8):
    nx = x_idx + dx[i]
    ny = y + dy[i]

    if nx > 8 or nx < 1 or ny > 8 or ny < 1:
        continue
    else:
        cnt += 1

print(cnt)