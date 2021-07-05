#P.92 큰 수의 법칙 
# 어떠한 배열에서 M번을 더하지만 같은 요소를 k번 이상 사용하지 않도록 하여 가장 큰 수를 만들어내는 알고리즘
N,M,K =map(int,input().split())
List=list(map(int,input().split()))
result=0
flag=0
a=len(List)
List.sort()
#제일 큰거 두개만 가지고 놀면 되는거자나
#제일 큰게 한개인지! 체크만 하면 괜찮다.
if List.count(List[a-1])==1:
  for i in range(M):
    flag+=1
    if flag<=(K):
      result+=List[a-1]
    else :
      result+=List[a-2]
      flag=0
else:
  for i in range(M):
    result+=List[a]
print(result)
