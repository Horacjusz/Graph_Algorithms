def bridges(G) :
    V = len(G)
    times = [0] * V
    parent = [None] * V
    visited = [False] * V
    low = [0] * V
    
    bridges = []
    def DFSVisit(G,s) :
        nonlocal time,bridges
        time += 1
        visited[s] = True
        times[s] = time
        low[s] = time
        for v in G[s] :
            if not visited[v] :
                parent[v] = s
                DFSVisit(G,v)
            if v != parent[s] :
                low[s] = min(low[s],low[v])
        if low[s] == times[s] and parent[s] is not None :
            bridges.append((parent[s],s))
        
    time = 0
    for v in range(V) :
        if not visited[v] :
            DFSVisit(G,v)
    return bridges
        
G = [[1,2],[0,3],[0,3],[1,2,4],[3,5,6],[4,6],[4,5,7],[6,8],[7]]

print(bridges(G))