n, m, k = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort(reverse=True)

first_num, second_num = numbers[0], numbers[1]
cnt = 0
_sum = 0

for i in range(m):
    if cnt == k:
        _sum += second_num
        cnt = 0
        continue
    _sum += first_num
    cnt += 1

print(_sum)