from collections import deque

def BFS(G,s) :
    V = len(G)
    visited = [False] * V
    parent = [None] * V
    distance = [float('inf')] * V
    
    Q = deque()
    Q.append(s)
    visited[s] = True
    
    while Q :
        v = Q.popleft()
        dist = distance[v] + 1
        
        for n in G[v] :
            if visited[n] :
                continue
            visited[n] = True
            distance[n] = dist
            parent[n] = v
            Q.append(n)
    
    print(distance)
    