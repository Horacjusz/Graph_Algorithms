graph = [[1,2], [0, 6, 3, 4, 2, 5], [1, 0, 6, 3, 4, 5], [1, 2, 4, 5], [1, 2, 3, 5], [1, 2, 3, 4], [1,2] ]
graph = [[1, 2, 3, 4], [0, 2, 3, 4], [0, 1, 3, 4], [0, 1, 2, 4], [0, 1, 2, 3]]
#graph = [[1,2],[0,2],[0,1]]
graph = [[3,5],[2,5,6,7],[1,4,5,7],[0,6],[2,7],[0,1,2,7],[1,3],[1,2,4,5]]

def euler(G, s = 0) :
    V = len(G)
    visited = [False] * V
    path = []
    
    def pathfinder(G,s) :
        nonlocal path
        visited[s] = True
        for v in G[s] :
            G[s].remove(v)
            G[v].remove(s)
            pathfinder(G,v)
        path.append(s)

    zeros = 0
    continuity = 0
    
    for v in range(V) :
        i = G[v]
        if len(i) == 0 :
            zeros += 1
            continue
        if (len(i) % 2) != 0 :
            return None
        if continuity == 0 :
            pathfinder(G,s)
            continuity += 1
        if not visited[v] :
            pathfinder(G,v)
            continuity += 1

    if continuity - zeros > 1 :
        return None
    
    return path

print(euler(graph))