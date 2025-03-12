from dimacs import *
from data import runtests
from collections import deque


def reading(name) :
    
    name = "problems\\" + name
    path = ""
    f = open( name + ".path", "r" )
    
    sign = f.read(1)
    while sign != "\n" :
        path += sign
        sign = f.read(1)
    
    (V,edges) = loadWeightedGraph( name + ".graph" )
    
    solution = (readSolution(name + ".graph") == "True")
    
    return V,edges,path,solution
    



def connotation( M ) :
    def bfs(graph, match, dist):
        """Przeszukiwanie wszerz do znalezienia najkrótszych ścieżek powiększających."""
        queue = deque()
        for u in range(1, len(dist) - 1):
            if match[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        dist[0] = float('inf')
        while queue:
            u = queue.popleft()
            if u != 0:
                for v in graph[u]:
                    if dist[match[v]] == float('inf'):
                        dist[match[v]] = dist[u] + 1
                        queue.append(match[v])
        return dist[0] != float('inf')

    def dfs(graph, match, dist, u):
        """Przeszukiwanie w głąb do aktualizacji skojarzeń."""
        if u != 0:
            for v in graph[u]:
                if dist[match[v]] == dist[u] + 1 and dfs(graph, match, dist, match[v]):
                    match[v] = u
                    match[u] = v
                    return True
            dist[u] = float('inf')
            return False
        return True

    def hopcroft_karp(graph, n, m):
        """Algorytm Hopcrofta-Karpa do znalezienia maksymalnego skojarzenia."""
        match = [0] * (n + m + 1)
        dist = [0] * (n + m + 1)
        matching = 0
        while bfs(graph, match, dist):
            for u in range(1, n + 1):
                if match[u] == 0 and dfs(graph, match, dist, u):
                    matching += 1
        return matching

    n = len(M)  # Liczba wierzchołków po jednej stronie
    m = max(max(l) for l in M) + 1  # Maksymalny indeks wierzchołka po drugiej stronie

    # Tworzenie grafu
    graph = {i: [] for i in range(1, n + m + 1)}
    for i, l in enumerate(M, start=1):
        for j in l:
            graph[i].append(n + j + 1)  # Dodanie krawędzi z odpowiednim przesunięciem
    
    return hopcroft_karp(graph, n, m)



def is_subtree_of(A,B,a,b) :
    A_parents = [None]*len(A)
    B_parents = [None]*len(B)
    
    bijection = [(b,a)]

    def check_subtree(a,b,pairs = [],level = 0) :
        nonlocal A, B, A_parents, B_parents, bijection
        
        header = ''
        for _ in range(level) :
            header += "-"
        header += ">"
        
        if len(B[b]) > len(A[a]) : return False
        
        occupied = []
        
        pairs = []
        
        for b_child in B[b] :
            if b_child == B_parents[b] : continue
            B_parents[b_child] = b
            match_found = False
            for a_child in A[a] :
                if a_child == A_parents[a] : continue
                if a_child in occupied : continue
                A_parents[a_child] = a
                if check_subtree(a_child,b_child,level = level+1) :
                    # occupied.append(a_child)
                    match_found = True
                    pairs.append((b_child,a_child))
            if not match_found : return False
        
        known_bs = []
        known_as = []
        
        if len(pairs) == 0 : return True
        known_bs = []
        known_as = []
        
        M = []
        
        for b_s,a_s in pairs :
            # if b_s not in B[b] or a_s not in A[a] : continue
            
            bID = 0
            for _ in range(len(known_bs)) :
                if known_bs[bID] == b_s : break
                bID += 1
            if bID == len(known_bs) :
                known_bs.append(b_s)
                M.append([])
    
            aID = 0
            for _ in range(len(known_as)) :
                if known_as[aID] == a_s : break
                aID += 1
            if aID == len(known_as) :
                known_as.append(a_s)
            M[bID].append(aID)
        # print(M)
        if len(known_bs) > len(known_as) : return False
        
        if len(B[b]) == 1 :
            count = connotation( M )
            # print(count,len(B[b]))
            
            return count == len(B[b])
        
        # print(header,b,a,pairs)
        
        return True
    
    return check_subtree(a,b)
    

def my_solve(N, entrance, corridors, path):
    # print(f"Komnaty: {N}, korytarze: {len(corridors)}")

    # for c in path.split(" "):
    #     ...
    
    
    graph = [[] for _ in range(N)]
    graph_edges_count = 0
    for corridor in corridors :
        if corridor[0] == entrance or corridor[1] == entrance : continue
        graph_edges_count += 1
        graph[corridor[0] - 1].append(corridor[1] - 1)
        graph[corridor[1] - 1].append(corridor[0] - 1)


    path_steps = []
    V_G = 1
    for step in path :
        if step == " " : continue
        if step == "+" : V_G += 1
        path_steps.append(step)


    G = [[] for _ in range(V_G)]

    G_parents = [None for _ in range(V_G)]

    placeholder = 0
    current = 0

    for step in path_steps :
        # print(step,current,placeholder)
        if step == "+" :
            current += 1
            
            G_parents[current] = placeholder
            G[placeholder].append(current)
            G[current].append(placeholder)
            placeholder = current
            
        elif step == "^" :
            
            placeholder = G_parents[placeholder]
            
        else :
            st = int(step)
            if placeholder == 0 : st -= 1
            # print(st,placeholder)
            placeholder = G[placeholder][st]
    
    G_edges_count = V_G - 1
    
    # print("A = ",graph)
    # print("B = ",G)
    
    if G_edges_count > graph_edges_count or V_G > N : return False
    

    for v in range(N) :
        if v == entrance - 1 : continue
        if is_subtree_of(graph, G, v, 0) : return True
    
    return False

names = ["mix-large-invalid","maze-3d-invalid-med"]

name = "mix-large-invalid"

V,edges,path,solution = reading( name )

# for e in range(V) :
#     print(e,my_solve(V,e,edges,path))


runtests(my_solve)