n, m=map(int, input().split())
result=[0]*n
for _ in range(n):
    nums=list(map(int, input().split()))
    result[_]=min(nums)
print(max(result))