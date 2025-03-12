def DFS(G) :
    V = len(G)
    visited = [False] * V
    sort = []
    def DFSVisit(G,s) :
        nonlocal sort,visited
        visited[s] = True
        for v in G[s] :
            if not visited[v] :
                DFSVisit(G,v)
        sort.append(s)
    
    for v in range(V) :
        if not visited[v] :
            DFSVisit(G,v)
    
    return sort[::-1]

def topo_sort(G) :
    V = len(G)
    ind_table = DFS(G)
    D = [[] for _ in range(V)]
    for i in range(V) :
        for v in G[ind_table[i]] :
            D[i].append(ind_table.index(v))
    
    return D
    
G = [[1,2],[2,4],[],[],[3,6],[4],[]]

print(topo_sort(G))