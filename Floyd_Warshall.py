'''def floyd_warshall (G) :
    n = len(G)
    parents = [[None for _ in range(n)] for _ in range(n)]
    infinity = float('inf')
    distance = [[infinity for _ in range(n)] for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            if G[i][j] != 0 :
                distance[i][j] = G[i][j]
        distance[i][i] = 0
        parents[i][i] = i
            
    for z in range(n) :
        for x in range(n) :
            for y in range(n) :
                if distance[x][y] > distance[x][z] + distance[z][y] :
                    distance[x][y] = distance[x][z] + distance[z][y]
                    parents[x][y] = parents[z][y]
                    
    return distance,parents'''

def floyd_warshall(G): #reprezentacja macierzowa, O(V^3)
    n = len(G)
    distance = [[float("Inf") if G[v][u] == None else G[v][u] for u in range(n)] for v in range(n)]
    parent = [[None if G[v][u] == None else v for u in range(n)] for v in range(n)]
    for t in range(n): #powiększamy wszystko o wieszchołek t - {v0,v1,...,vn-1}
        for x in range(n):
            for y in range(n):
                distance[x][y] = min(distance[x][y],distance[x][t]+distance[t][y]) #opcja bez paretna, jest ładniej
                if distance[x][y] > distance[x][t] + distance[t][y]: #opcja z parentem
                    distance[x][y] = distance[x][t] + distance[t][y]
                    parent[x][y] = parent[t][y]