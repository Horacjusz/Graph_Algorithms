from collections import deque
from dimacs import *
from copy import deepcopy

name = "graphs-lab4\\chordal\\simple-noninterval2"

(V,L) = loadWeightedGraph( name )        # wczytaj graf
for (x,y,c) in L:                        # przeglądaj krawędzie z listy
    print( "krawedz miedzy", x, "i", y,"o wadze", c )   # wypisuj
    
S = 0
T = V - 1
    
def to_list(edges) :
    D = [[] for _ in range(V)]
    for u,v,_ in edges :
        D[u-1].append(v-1)
        D[v-1].append(u-1)
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
    
print_graph(list_form)



new_list = [[1,2],[0,3],[0],[1]]
# print_graph(list_form)
# print_graph(new_list)

# list_form = new_list
        

def lexBFS(G,s) :
    V = len(G)
    visited = [False] * V
    parents = [None] * V
    etiquettes = [[] for _ in range(V)]
    distances = [float('inf')] * V
    
    order = []
    
    distances[s] = 0
    visited[s] = True
    
    Q = deque()
    Q.append(s)
    
    
    def etiquette_compare(a,b) :
        nonlocal etiquettes,order
        if a > b : a,b = b,a
        e_a = etiquettes[a]
        e_b = etiquettes[b]
        
        small_e = e_a
        small = a
        large_e = e_b
        large = b
        if len(e_a) > len(e_b) :
            small_e,large_e = large_e,small_e
            small,large = large,small
        
        
        for i in range(len(small_e)) :
            b_ord = order.index(e_b[i])
            a_ord = order.index(e_a[i])
            if a_ord < b_ord :
                return a
            if b_ord < a_ord :
                return b 
        
        if len(e_a) == len(e_b) : return a
        else : 
            if large == a :
                return a
            else :
                return b
    
    while Q :
        v = Q.popleft()
        order.append(v)
        dist = distances[v]
        
        local_options = []
        
        for n in G[v] :
            if not visited[n] :
                local_options.append(n)
                etiquettes[n].append(v)
        local_options.sort()
        
        other_options = []
        for n in range(V) :
            if n not in local_options and not visited[n] :
                other_options.append(n)
        print(local_options,other_options)
        
        temp = None
        if local_options : temp = local_options[0]
        elif other_options : temp = other_options[0]
        if temp is None : 
            return order
        
        for i in range(1,V) :
            if visited[i] : continue
            temp = etiquette_compare(temp,i)
        print(temp)
            
        if temp is not None :
            Q.append(temp)
            distances[temp] = dist + 1
            parents[temp] = v
            visited[temp] = True
        
        
          
    # print(etiquettes)
    # print(order)

a = lexBFS(list_form,0)

for i in range(len(a)) :
    a[i] += 1
print(a)
for i in range(len(a)) :
    a[i] -= 1


def checkLexBFS(G, vs):
  n = len(G)
  pi = [None] * n
  for i, v in enumerate(vs):
    pi[v] = i

  for i in range(n-1):
    for j in range(i+1, n-1):
      new_list_i = []
      for _ in G[vs[i]] :
          new_list_i.append(_)
      new_list_j = []
      for _ in G[vs[j]] :
          new_list_j.append(_)
      
      Ni = set(new_list_i)
      Nj = set(new_list_j)

      verts = [pi[v] for v in Nj - Ni if pi[v] < i]
      if verts:
        viable = [pi[v] for v in Ni - Nj]
        if not viable or min(verts) <= min(viable):
          return False
  return True

# print(checkLexBFS(list_form,a),readSolution(name))

def is_clique(G,table) :
    for v in table:
        checker = deepcopy(table)
        checker.remove(v)
        for n in table :
            if n in G[v] :
                checker.remove(n)
        if checker :
            return False
    return True
            
            
def checkLexBFS2(G,result) :
    
    for v in result :
        checker_neighbours = [v]
        for n in result :
            if n == v : break
            if n in G[v] :
                checker_neighbours.append(n)
        for i in range(len(checker_neighbours)) :
            checker_neighbours[i] += 1
        print(v + 1,":",checker_neighbours)
        for i in range(len(checker_neighbours)) :
            checker_neighbours[i] -= 1
        if not is_clique(G,checker_neighbours) : return False
    return True
        
print()
b = checkLexBFS2(list_form,a)
solution = readSolution(name)
if solution == "1" : solution = True
else : solution = False
output = (b == solution)

print(b,solution)
print(output)
    