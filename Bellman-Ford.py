def bellman_ford(G, s):
    V = len(G)
    distance = [float('inf')] * V
    distance[s] = 0
    
    for _ in range(V - 1):
        for v in range(V):
            for u,val in G[v]:
                value = distance[v] + val
                if distance[u] > value:
                     distance[u] = value
     
    for v in range(V):
        for u,val in G[v]:
            if distance[u] > distance[v] + val:
                return False
    return distance

graph = [[(2,-1)],[(0,-1)],[(1,1)]]

print(bellman_ford(graph, 0))

