from collections import deque

def BFS(G,s,t,parent) :
    V = len(G)
    visited = [False] * V
    
    Q = deque()
    Q.append(s)
    
    while Q :
        v = Q.popleft()
        visited[v] = True
        if v == t :
            break
        for n in range(V) :
            w = G[v][n]
            if not visited[n] and w > 0 :
                parent[n] = v
                Q.append(n)
    
    if visited[t] :
        return True
    
    return False
                
def eddmonds_karp(G,s,t) :
    V = len(G)
    parent = [None]*V
    max_flow = 0
    while BFS(G,s,t,parent) :
        flow = float('inf')
        v = t
        while v != s :
            flow = min(flow,G[parent[v]][v])
            v = parent[v]
        max_flow += flow
        v = t
        while v != s :
            u = parent[v]
            G[u][v] -= flow
            G[v][u] += flow
            v = u
    return max_flow
            
            
        
            
    
G = [[0 for j in range(6)] for i in range(6)]
G[0][1] = 4
G[0][3] = 3
G[1][2] = 2
G[1][3] = 2
G[2][5] = 4
G[3][2] = 2
G[3][4] = 2
G[4][5] = 5

print(eddmonds_karp(G,0,len(G)-1))