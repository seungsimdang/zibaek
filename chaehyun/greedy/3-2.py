n, m, k = map(int, input().split())
nums=list(map(int, input().split()))
nums.sort(reverse=True)
sum=0
cnt=0
for i in range (m):
    if cnt==k:
        cnt=0
        sum+=nums[1]
    else: sum+=nums[0]
    cnt+=1
print(sum)