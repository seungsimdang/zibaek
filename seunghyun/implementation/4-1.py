n = int(input())
plan = list(input().split())

currPos = [1, 1]

def move(input, pos):
    y, x = pos[0], pos[1]

    if input == 'L':
        x -= 1
    elif input == 'R':
        x += 1
    elif input == "U":
        y -= 1
    elif input == "D":
        y += 1

    return [y, x]

for i in plan:
    newPos = move(i, currPos) # call by ref

    if newPos[0] < 1 or newPos[0] > n or newPos[1] < 1 or newPos[1] > n:
        continue
    currPos = newPos


print(currPos[0], currPos[1])