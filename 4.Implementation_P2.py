N=int(input())

x=0
y=0
def input_D(A):
  global x,y
  if A=='L':
    if y<1:
      pass
    else:
      y-=1
  elif A=='R':
    if y==(N-1):
      pass
    else:
      y+=1
  elif A=='U':
    if x<1:
      pass
    else:
      x-=1
  elif A=='D':
    if x==(N-1):
      pass
    else:
      x+=1
  else:
    pass

A=list(map(str,input().split()))
print(A)
print(len(A))
for i in range(len(A)):
  input_D(A[i])

print (x+1,y+1)
