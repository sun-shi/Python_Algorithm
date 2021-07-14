# 왕실의 나이트
A=input()
garo=['a','b','c','d','e','f','g','h']
saero=[1,2,3,4,5,6,7,8]
x=garo.index(A[0])
y=saero.index(int(A[1])) #입력값에 대한 좌표 구함.
count=0
steps=[[-2,+1],[-2,-1],[+2,-1],[+2,+1],[+1,-2],[+1,+2],[-1,+2],[-1,-2]]
for i in range(len(steps)):
    nx=x+steps[i][0]
    ny=y+steps[i][1]
    if (nx>=0) and (nx<=7) and (ny>=0)and(ny<=7):
        count+=1

print(count)
    
