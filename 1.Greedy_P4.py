N,K=map(int,input().split())
count=0
while True:
    if N>=K:
        tN=N//K
        N=N-(tN*K)
        count+=tN
        
    elif N<K:
        N=N-1
        count+=1
        continue
    elif N==1:
        break
    else:
        pass

    print(count)
        
