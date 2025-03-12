#Works on list graph representation

# 0=====5=====2\\
# |          ||  6
# |          ||   \\
# 8          2     4
# |          ||   /
# |          || 9
# 1=====3=====3/

graph = [[(1,8), (2, 5)], [(0, 8), (3, 3)], [(0, 5), (3, 2), (4, 6)], [(1, 3), (2, 2), (4, 9)], [(2, 6), (3, 9)]]

def find(v, parents):
    
    while parents[v] != v :
        v = parents[v]
    return parents[v]

def union(x, y, parents, rank):
    x = find(x, parents)
    y = find(y, parents)
    if rank[x] > rank[y]:
        parents[y] = x
        return x
    else :
        parents[x] = y
        if rank[y] == rank[x]:
            rank[y] +=1
        return y

def kruskal(G,root = 0):
    V = len(G)
    parents = [i for i in range(V)]
    rank = [0] * V
    edges = []
    MST = []
    for s in range(V):
        for v, c in G[s]:
            edges.append((s, v, c))
    edges.sort(key = lambda x: x[2])
    print("edges",edges)
    E = len(edges)
    for i in range(E):
        if len(MST) >= V-1 :
            break
        u = edges[i][0]
        v = edges[i][1]
        x = find(u, parents)
        y = find(v, parents)
        if x != y:
            MST.append((u, v, edges[i][2]))
            union(x, y, parents, rank)
    print("parents")
    for v in range(V) :
        print(parents[v])
    return MST

print(kruskal(graph))