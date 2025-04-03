n, m = map(int, input().split())

max_num = 0
for _ in range(n):
    cards = list(map(int, input().split()))
    cards.sort()
    
    max_num = max(max_num, cards[0])

print(max_num)