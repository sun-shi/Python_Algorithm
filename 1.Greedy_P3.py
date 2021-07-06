N,M=map(int,input().split())
cards=[]
i=0
j=0
for i in range(N):
  cards.append(list(map(int,input().split())))
  cards[i].sort()
  if i==(N-1):
    result=cards[N-1][0]
    for j in range(N-1):
      if cards[j][0]>result:
        result=cards[j][0]
      

print(result)
