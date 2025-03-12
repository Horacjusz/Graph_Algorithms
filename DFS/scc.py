def DFS(G,track = [], coherence = False) :
    V = len(G)
    times = [float('inf')] * V
    parent = [None] * V
    visited = [False] * V
        
    def DFSVisit(G,s) :
        nonlocal time,new_visited
        time += 1
        visited[s] = True
        times[s] = time
        for v in G[s] :
            if not visited[v] :
                parent[v] = s
                new_visited.append(v)
                DFSVisit(G,v)
                
    time = 0
    if len(track) == 0 and not coherence :
        track = [i for i in range(V)]
    
    coherent = []
    for u in track :
        if not visited[u] :
            new_visited = [u]
            DFSVisit(G,u)
            coherent.append(new_visited)
    
    if coherence :
        return coherent
    
    return times

def scc(G) :
    V = len(G)
    D = [[] for _ in range(V)]
    for i in range(V) :
        for v in G[i] :
            D[v].append(i)
    
    track = DFS(G)
    trace = []
    for _ in range(V) :
        ind = track.index(max(track))
        track[ind] = 0
        trace.append(ind)
    
    return DFS(D,trace,True)



G = [[],[0],[0],[1,2]]
G = [[1],[11,3],[0],[2,4],[7],[4],[5],[6],[7,9],[10],[11],[8]]

print(scc(G))