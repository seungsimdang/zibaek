n, m = map(int, input().split())
pos_x, pos_y, direction = map(int, input().split())  # 0: 북, 1: 동, 2: 남, 3: 서
_map = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

cnt = 1
visited[pos_y][pos_x] = 1

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

while True:
    turned = False  # 4방향 중 갈 수 있는 방향을 찾았는지 여부

    for _ in range(4):
        direction = (direction + 3) % 4  # 왼쪽 회전
        next_pos_x = pos_x + dx[direction]
        next_pos_y = pos_y + dy[direction]

        if 0 <= next_pos_x < m and 0 <= next_pos_y < n and _map[next_pos_y][next_pos_x] == 0 and visited[next_pos_y][next_pos_x] == 0:
            pos_x, pos_y = next_pos_x, next_pos_y
            visited[pos_y][pos_x] = 1
            cnt += 1

            turned = True
            break

    # 네 방향 모두 이동 못함 -> 뒤로 한 칸
    if not turned:
        back_dir = (direction + 2) % 4
        back_pos_x = pos_x + dx[back_dir]
        back_pos_y = pos_y + dy[back_dir]

        if 0 <= back_pos_x < m and 0 <= back_pos_y < n and _map[back_pos_y][back_pos_x] == 0:
            pos_x, pos_y = back_pos_x, back_pos_y
        else:
            break

print(cnt)