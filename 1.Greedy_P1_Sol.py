
N,M,K =map(int,input().split())
data=list(map(int,input().split()))
data.sort()
first=data[n-1]
second=data[n-2]

count = int(M/(K+1))*K
count+=M%(K+1)

result=0
result+=(count)*first
result+=(M-count)*second

print(result)

# 하나의 묶음 단위로 본 경우.
