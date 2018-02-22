


coins=[1,2,5,10,20,50,100,200]
noc=len(coins)
sum=200
ways=[[0 for j in range(sum+1)] for i in range(noc+1)]
for i in range(noc+1):
    ways[i][0]=1
for j in range(1,sum):
    ways[0][j]=0
    
k=0    
for i in range(1,noc+1):
    for j in range(1,sum+1):
        p=j-coins[k]
        if p>=0:
            ways[i][j]=ways[i-1][j]+ways[i][p]
        else:
            ways[i][j]=ways[i-1][j]
                
    
    k=k+1



print(ways[noc][sum])
