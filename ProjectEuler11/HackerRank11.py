import sys


grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)

#Right
m1=0
for g in grid:
    for i in range(len(g)-3):
        m1=max(m1,g[i]*g[i+1]*g[i+2]*g[i+3])
                
#Down
m2=0
for i in range(len(grid[0])):
    for j in range(len(grid)-3):
        m2=max(m2,grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3])
        
#Diagonal
m3=0
for j in range(len(grid)-3):
    for i in range(len(grid[0])-3):
        m3=max(m3,grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3])    
        
m4=0
for j in range(len(grid)-3):
    for i in range(3,len(grid[0])):
        m3=max(m3,grid[i][j]*grid[i-1][j+1]*grid[i-2][j+2]*grid[i-3][j+3])             
                
print(max(m1,m2,m3,m4))                
