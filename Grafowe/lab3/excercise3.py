from collections import deque
from dimacs import *
from copy import deepcopy
from excercise2 import ford

name = "graphs-lab2\\connectivity\\grid100x100"

(V,L) = loadWeightedGraph( name )        # wczytaj graf
# for (x,y,c) in L:                        # przeglądaj krawędzie z listy
#     print( "krawedz miedzy", x, "i", y,"o wadze", c )   # wypisuj
    
S = 0
T = V - 1
    
def to_list(edges) :
    D = [[] for _ in range(V)]
    for u,v,w in edges :
        D[u-1].append([v-1,w])
        D[v-1].append([u-1,w])
    return D

def to_matrix(edges) :
    D = [[0 for _ in range(V)] for _ in range(V)]
    for u,v,w in edges :
        D[u-1][v-1] = w
        D[v-1][u-1] = w
        
    return D

list_form = to_list(L)
matrix_form = to_matrix(L)

def print_graph(G) :
    print("===")
    for _ in G :
        print(_)
    print("===")
    
# print_graph(list_form)

def connectivity_flow(G) :
    
    conn = float('inf')

    for u in range(V) :
        for v in range(V) :
            conn = min(conn,ford(deepcopy(G),u,v))

    return conn

# print(connectivity_flow(list_form),readSolution(name))


def stoer_wagner_matrix(graph) :
    
    def max_edge(G) :
        vertex,neighbour,weight = None,None,float('-inf')
        for i in range(len(G)) :
            for j in range(i,len(G)) :
                if i == j : continue
                if G[i][j] > weight : 
                    vertex,neighbour,weight = i,j,G[i][j]
        return vertex,neighbour
    
    def vertex_merge(D, vertex, new, popped = []) :
        G = deepcopy(D)
        for i in range(len(G)-1,-1,-1) :
            G[vertex][i] += G[new][i]
            G[i][vertex] += G[i][new]
            G[i][i] = 0
            G[i].pop(new)
        G.pop(new)
        popped.append(new)
        if vertex > new : vertex -= 1
        return G,vertex,popped
    
    def checking(G,vertex = None, popped = []) :
        neighbour = None
        if vertex is None :
            vertex,neighbour = max_edge(G)
        else :
            maximum = float('-inf')
            for i in range(len(G)) :
                if G[vertex][i] > maximum :
                    maximum = G[vertex][i]
                    neighbour = i
        
        return vertex_merge(G,vertex,neighbour,popped)
        
    
    G = deepcopy(graph)
    
    cut = float('inf')
    
    while len(G) > 2 :    
        D = deepcopy(G)
        vertex = None
        popped = []
        while len(D) > 2 :
            D,vertex,popped = checking(D,vertex,popped)
        cut = min(cut,D[0][1])
        
        popped.reverse()
        ind = 1
        phantom = [len(G) - 1,0]
        while popped :
            phantom.insert(popped.pop(),ind)
            ind += 1
        
        v,n = None,None
        for i in range(len(phantom)) :
            if phantom[i] - 2 < 0 :
                if v is None : v = i
                else : 
                    n = i
                    break
                
        G,_,_ = vertex_merge(G,v,n)
           
    return cut

print("=")
print(stoer_wagner_matrix(matrix_form),readSolution(name))


# def stoer_wagner(graph) :
    
#     def max_edge(G) :
#         vertex, neighbour_index ,weight = None,None,float('-inf')
#         for v in range(len(G)) :
#             for i in range(len(G[v])) :
#                 _, w = G[v][i]
#                 if w > weight :
#                     vertex,neighbour_index,weight = v,i,w
#         return vertex,neighbour_index
    
#     def vertex_merge(D,vertex, neighbour, popped = []) :
#         G = deepcopy(D)
#         for i in range(len(G[vertex])) :
#             if G[vertex][i][0] == neighbour : 
#                 G[vertex].pop(i)
#                 break
        
#         for n,w in G[neighbour] :
#             if n == vertex : continue
#             breaking = False
#             for i in range(len(G[vertex])) :
#                 if G[vertex][i][0] == n : 
#                     G[vertex][i][1] += w
#                     breaking = True
#                     break
#             if not breaking :
#                 G[vertex].append([n,w])
                
#         actual_vertex = vertex
#         if vertex > neighbour :
#             actual_vertex -= 1
        
#         for v in range(len(G)) :
#             if v == neighbour : continue
#             n_ind = None
#             v_ind = None
#             summed = 0
            
#             for i in range(len(G[v])) :
#                 n,w = G[v][i]
#                 if n > neighbour : G[v][i][0] -= 1
#                 if n == neighbour :
#                     n_ind = i
#                     summed += w
#                 if n == vertex :
#                     v_ind = i
#                     summed += w
            
#             if v_ind is not None :
#                 G[v][v_ind][1] = summed
#             elif n_ind is not None :
#                 G[v].append([actual_vertex,summed])
            
#             if n_ind is not None : G[v].pop(n_ind)
#         G.pop(neighbour)
#         popped.append(neighbour)
        
#         return G,actual_vertex,popped
    
    
#     def checking(D,vertex = None,popped = []) :
#         G = deepcopy(D)
#         neighbour_index = None
        
#         if vertex is None :
#             vertex,neighbour_index = max_edge(G)
#         else :
#             max_weight = float('-inf')
#             for i in range(len(G[vertex])) :
#                 if G[vertex][i][1] > max_weight :
#                     max_weight = G[vertex][i][1]
#                     neighbour_index = i
        
#         neighbour = G[vertex][neighbour_index][0]
        
        
#         G,vertex,popped = vertex_merge(G,vertex,neighbour,popped)
        
        
#         return G,vertex,popped
        
#     G = deepcopy(graph)

#     cut = float('inf')

#     while len(G) > 2 :

#         D = deepcopy(G)
#         vertex = None
#         popped = []
#         while len(D) > 2 :
#             D,vertex,popped = checking(D,vertex,popped)
        
#         cut = min(cut,D[0][0][1])
        
#         popped.reverse()
#         ind = 1
#         phantom = [len(G) - 1,0]
#         while popped :
#             phantom.insert(popped.pop(),ind)
#             ind += 1
        
#         n,v = None,None
#         for i in range(len(phantom)) :
#             if phantom[i] - 2 < 0 :
#                 if n is None : n = i
#                 else : v = i
        
#         G,_,_ = vertex_merge(G,n,v)

#     return cut
    
# print('=====')   
# print(stoer_wagner(list_form),readSolution(name))