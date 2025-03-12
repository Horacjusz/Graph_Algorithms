from collections import deque

def BFS(G,s,t) :
    V = len(G)
    visited = [False for _ in range(V)]
    parent = [None for _ in range(V)]
    visited[s] = True
    Q = deque()
    Q.append(s)
    breaking = False
    while Q :
        v = Q.popleft()
        idx = 0
        for n,cap,flow in G[v] :
            if visited[n] or (cap - flow == 0) :
                idx += 1
                continue
            visited[n] = True
            parent[n] = v
            if n == t :
                breaking = True
                break
            Q.append(n)
            idx += 1
            
        if breaking :
            break
    
    if not visited[t] :
        return []
    
    path = [t]
    c = parent[t]
    while parent[c] is not None :
        path = [c] + path
        c = parent[c]
    print(path)
        
    return path


def edmonds_karp(G,s,t) :
    V = len(G)
    max_flow = 0
    path = BFS(G,s,t)
    
    while path :
        prev = s
        minimum = float('inf')
        idx_table = []
        for i in path :
            j = 0
            while G[prev][j][0] != i :
                j += 1
            idx_table += [j]
            minimum = min(minimum,G[prev][j][1] - G[prev][j][2])
            prev = i
        
        max_flow += minimum
        prev = s
        idx = 0
        for i in path :
            id2 = G[prev][idx_table[idx]][0]
            G[prev][idx_table[idx]][2] += minimum
            j = 0
            while G[id2][j][0] != prev :
                j += 1
            G[id2][j][2] -= minimum
            idx += 1
            prev = i
        
        for i in G :
            print(i)
        
        print('---')
        path = BFS(G,s,t)
    
    return max_flow

def add_edge(G,u,v,capacity,flow) :
    G[u].append([v,capacity,flow])
    G[v].append([u,capacity,flow])

def graph_create(M) :
    n = len(M)
    G = [[] for _ in range(2*(n+1))]
    s = 0
    t = 2*n + 1
    for i in range(n) :
        u = 2*i + 1
        v = u + 1
        add_edge(G,s,u,1,0)
        add_edge(G,v,t,1,0)
        for j in M[i] :
            v = 2*(j + 1)
            add_edge(G,u,v,1,0)
    return G

M = [[0, 1, 3], [2, 4], [0, 2], [3], [3, 2]]

G = graph_create(M)
G = [[[1,1,0],[2,1,0]],
    [[0,1,0],[3,1,0],[4,1,0]],
    [[0,1,0],[4,1,0]],
    [[1,1,0],[5,1,0]],
    [[1,1,0],[2,1,0],[5,1,0]],
    [[3,1,0],[4,1,0]]]

for i in G :
    print(i)
    
print("===")
print(edmonds_karp(G,0,5))
#print(edmonds_karp(G,0,2*len(M) + 1))