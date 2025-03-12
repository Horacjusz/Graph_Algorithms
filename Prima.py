import heapq

def prima(G,s = 0) :
    V = len(G)
    Q = [(0, s)]
    parents = [None] * V
    mins = [float('inf')] * V
    mins[s] = 0
    visited = [False] * V
    counter = 0
    
    while counter < V :
        v = heapq.heappop(Q)[1]
        if visited[v] : continue
        
        for n, val in G[v] :
            if visited[n] : continue
            
            if mins[n] > val :
                mins[n] = val
                parents[n] = v
                heapq.heappush(Q, (val, n))
        visited[v] = True
        counter += 1
    
    return parents

                        
test = [[(1,3),(2,4)],[(0,3),(4,3)],[(5,1),(3,3),(0,4)],[(2,3),(4,5)],[(1,3),(5,2),(3,5)],[(4,2),(2,1),(6,3)],[(5,3),(7,6)],[(6,6)]]
test2 = [[(1,1),(4,5),(5,8)], [(0,1),(2,3)], [(1,3),(3,6),(4,4)], [(2,6),(4,2)], [(0,5),(4,4),(3,2),(5,7)], [(0,8),(4,7)]]
test2 = [[(1,8), (2, 5)], [(0, 8), (3, 3)], [(0, 5), (3, 2), (4, 6)], [(1, 3), (2, 2), (4, 9)], [(2, 6), (3, 9)]]

print(prima(test2,0))