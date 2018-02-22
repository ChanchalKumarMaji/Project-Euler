import heapq

Adjacency_Matrix=[['-', 16, 12, 21, '-', '-', '-'],
                  [16, '-', '-', 17, 20, '-', '-'],
                  [12, '-', '-', 28, '-', 31, '-'],
                  [21, 17, 28, '-', 18, 19, 23],
                  ['-', 20, '-', 18, '-', '-', 11],
                  ['-', '-', 31, 19, '-', '-', 27],
                  ['-', '-', '-', 23, 11, 27, '-']]




def ShortestPath(s):    #assuming the source is s
    n=len(Adjacency_Matrix)
    visited=[False for i in range(n)]    #n is the total number of vertices
    distance=[100000 for i in range(n)]    # setting the distance to infinty or very large
    Q=[]
    distance[s]=0
    heapq.heappush(Q,(distance[s],s))
    
    
    
    #parent=[0 for i in range(n)]
    
    while Q:
        a=(heapq.heappop(Q))[1]
        if visited[a]:
            continue
        visited[a]=True
        l=len(Adjacency_Matrix[a])
        for b in range(l):    
            w=Adjacency_Matrix[a][b]
            if w!='-':
                if distance[a]+w<distance[b]:
                    distance[b]=distance[a]+w
                    #parent[b]=a
                heapq.heappush(Q,(distance[b],b))

            
    print(distance)
    print(max(distance)) 
    #print(parent)       
                    

ShortestPath(0) 
           
