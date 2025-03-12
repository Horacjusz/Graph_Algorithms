import heapq
from dimacs import *
S = 0
T = 1

name = "graphs\\clique5"

(V,L) = loadWeightedGraph( name )        # wczytaj graf
#for (x,y,c) in L:                        # przeglądaj krawędzie z listy
#    print( "krawedz miedzy", x, "i", y,"o wadze", c )   # wypisuj


L.sort(key = lambda x: x[2],reverse = True)
print(V,L)
solution = int(readSolution(name))

def find(v, parents):
    while parents[v] != v :
        v = parents[v]
    return parents[v]

def union(u, v, parents, rank):
    x = find(u, parents)
    y = find(v, parents)
    if rank[x] > rank[y]:
        parents[y] = x
        parents[v] = x
        rank[y] += 1
        return x
    else :
        parents[x] = y
        parents[u] = y
        if rank[y] == rank[x] :
            rank[y] += 1
        return y
    
def connect(edges) :
    parents = [i for i in range(V)]
    rank = [0]*V
    path = []
    for u,v,w in edges :
        x = find(u-1,parents)
        y = find(v-1,parents)
        if x != y :
            path.append((u,v,w))
            union(x,y,parents,rank)
        if find(parents[S], parents) == find(parents[T], parents) :
            return w

find_union_result = connect(L)
print(solution,find_union_result)  
if solution == find_union_result :
    print("Find-Union Passed")
else : print("Find-Union Failed")

def to_list(edges) :
    D = [[] for _ in range(V)]
    for u,v,w in edges :
        D[u-1].append((v-1,w))
        D[v-1].append((u-1,w))
    return D

list_form = to_list(L)
weight_list = []
for u,v,w in L :
    weight_list.append(w)

def bisect(start,end,G) :
    global S,T,weight_list
    if start == end :
        return start
    while start != end :
        index = round((end - start) // 2) + start
        weight = weight_list[index]
        if end - start == 1 :
            index += 1
        if specific_DFS(G,weight,S,T) :
            end = index
        else :
            start = index
            
    return weight_list[index]

def specific_DFS(G,value,s,t) :
    V = len(G)
    times = [float('inf')] * V
    parent = [None] * V
    visited = [False] * V
    def DFSVisit(G,s) :
        nonlocal time,visited
        time += 1
        visited[s] = True
        times[s] = time
        for v,w in G[s] :
            if not visited[v] and w >= value :
                parent[v] = s
                DFSVisit(G,v)
        
    time = 0
    counter = 0
    for v in range(V) :
        if not visited[v] :
            counter += 1
            DFSVisit(G,v)
            if visited[s] and visited[t] :
                return True
            visited = [False] * V    
    return False

DFS_bisect_result = bisect(0,V-1,list_form)
print(solution,DFS_bisect_result)  
if solution == DFS_bisect_result :
    print("DFS bisect Passed")
else : print("DFS bisect Failed")

def specific_dijkstra(G,s,t) :
    V = len(G)
    max_height = [0] * V
    parents = [None for _ in range(V)]
    distances = [float('inf')] * V
    distances[s] = 0
    print(G)
    
    Q = [(0,s)]
    
    while Q :
        _, v = heapq.heappop(Q)
        dist = distances[v]
        print(_,v)
        print(max_height)
        
        for n,val in G[v] :
            if n == parents[v] :
                continue
            
            print("t",max_height[t],val)
            max_height[n] = max(max_height[n],val)
            
            distance = dist + val
            if distance < distances[n] :
                distances[n] = distance
                parents[n] = v
                heapq.heappush(Q, (-distance, n))
    return max_height[t]

dijkstra_result = specific_dijkstra(list_form,S,T)
print(solution,dijkstra_result)  
if solution == dijkstra_result :
    print("Dijkstra Passed")
else : print("Dijkstra Failed")

for _ in list_form :
    print(_)