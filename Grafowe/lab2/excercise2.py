from collections import deque
from dimacs import *

name = "graphs-lab2\\flow\\grid100x100"

(V,L) = loadDirectedWeightedGraph( name )        # wczytaj graf
# for (x,y,c) in L:                        # przeglądaj krawędzie z listy
    # print( "krawedz miedzy", x, "i", y,"o wadze", c )   # wypisuj
    
S = 0
T = V - 1
    
def to_list(edges) :
    D = [[] for _ in range(V)]
    for u,v,w in edges :
        D[u-1].append([v-1,w,0])
        D[v-1].append([u-1,0,w])
        
    return D
    

list_form = to_list(L)

 
def ford(G, s, t):
    V = len(G)
    flow = 0
    parent = [None]*V
    
    while BFS(G, s, t, parent) :
        v = t
        path_flow = float('inf')
        
        while v != s:
           u = parent[v]
           ind = None    
           for i in range(len(G[u])) :
               if G[u][i][0] == v :
                   if G[u][i][1] > 0: 
                       ind = i
                       break
           path_flow = min(path_flow, G[u][ind][1])
           v = parent[v]
        flow += path_flow
        v = t
        while v != s:
            u = parent[v]   
            indu = None         
            for i in range(len(G[u])) :
                if G[u][i][0] == v :
                    indu = i
                    break
            indv = None
            for i in range(len(G[v])) :
                if G[v][i][0] == u :
                    indv = i
                    break
            
            G[u][indu][1] -= path_flow
            G[u][indu][2] += path_flow
           
            G[v][indv][1] += path_flow
            G[v][indv][2] -= path_flow
            v = parent[v]
        parent = [None]*V
        
    return flow

def BFS(G, s, t, parent):
    V = len(G)
    visited = [False] * V
    Q = deque()
    Q.append(s)
    visited[s] = True
    while Q :
        v = Q.popleft()
        for n,w,_ in G[v] :
            if visited[n] == False and w > 0 :
                visited[n] = True
                parent[n] = v
                Q.append(n)
    return visited[t]


a = ford(list_form, S, T)
print(a,readSolution(name)) 
