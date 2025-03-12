def articulation_points(G) :
    V = len(G)
    times = [0] * V
    parent = [None] * V
    visited = [False] * V
    low = [0] * V
    
    articulations = []
    def DFSVisit(G,s) :
        nonlocal time,low,visited,articulations,parent
        
        no_children = 0
        
        visited[s] = True
        times[s] = time
        low[s] = time
        time += 1
        for v in G[s] :
            if not visited[v] :
                parent[v] = s
                no_children += 1
                DFSVisit(G,v)
                low[s] = min(low[s],low[v])
                if parent[s] is None and no_children > 1 :
                    articulations.append(s)
                if parent[s] is not None and low[v] >= times[s] :
                    articulations.append(s)
            elif v != parent[s] :
                low[s] = min(low[s],times[v])  
       
    time = 0
    for v in range(V) :
        if not visited[v] :
            DFSVisit(G,v)
    
    return articulations

