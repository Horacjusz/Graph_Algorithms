from data import runtests
from dimacs import *


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


def check_way(G, s, path):
    V = len(G)
    
    parents = [None] * V
    model = [[] for _ in range(V)]
    
    def dfs(v, p):
        if p >= len(path):
            return True
        
        step = path[p]
        
        if step == "+":
            for n in G[v]:
                if n == parents[v] or n in model[v]:
                    continue
                # Zapamiętujemy zmiany, aby móc je cofnąć
                prev_parent = parents[n]
                parents[n] = v
                model[v].append(n)
                model[n].append(v)
                if dfs(n, p + 1):
                    return True
                # Cofamy zmiany (backtracking)
                parents[n] = prev_parent
                model[v].pop()
                model[n].pop()
                
        elif step == "^":
            if parents[v] is not None:
                return dfs(parents[v], p + 1)
                
        return False
    
    return dfs(s, 0)
    
    
def dfs_tree(D,s, tellsize = False,maximum = float('inf')) :
    tree = ""
    parents = [None]*len(D)
    
    stack = [("+",s)]
    
    max_distance = -1
    distance = -1
    
    while stack :
        step,v = stack.pop()
        if v != s : 
            tree += step + " "
        
        if step == "+" :
            distance += 1
            if distance > maximum : continue
            for n in D[v] :
                if n == parents[v] : continue
                parents[n] = v
                stack.append(("^",n))
                stack.append(("+",n))
        else :
            distance -= 1
        
        max_distance = max(max_distance,distance)
    
    if tellsize : return tree,max_distance
    
    return tree


def my_solve(N, entrance, corridors, path):
    # print(f"Komnaty: {N}, korytarze: {len(corridors)}")

    # for c in path.split(" "):
    #     ...
    
    G = [[] for _ in range(N)]
    G_edges_count = 0
    for corridor in corridors :
        if corridor[0] == entrance or corridor[1] == entrance : continue
        G_edges_count += 1
        G[corridor[0] - 1].append(corridor[1] - 1)
        G[corridor[1] - 1].append(corridor[0] - 1)
    
    path_steps = []
    V_graph = 1
    for step in path :
        if step == "+" : V_graph += 1
    path_steps = path.split(" ")


    path_graph = [[] for _ in range(V_graph)]

    path_parents = [None for _ in range(V_graph)]

    placeholder = 0
    current = 0

    for step in path_steps :
        if step == "+" :
            current += 1
            
            path_parents[current] = placeholder
            path_graph[placeholder].append(current)
            path_graph[current].append(placeholder)
            placeholder = current
            
        elif step == "^" :
            
            placeholder = path_parents[placeholder]
            
        else :
            st = int(step)
            if placeholder == 0 : st -= 1
            placeholder = path_graph[placeholder][st]
    
    
    simple_path = dfs_tree(path_graph,0)
    
    
    path_table = simple_path.split(" ")
    path_table.pop()

    for v in range(N) :
        if v == entrance - 1 : continue
        check = check_way(G,v,path_table)
        if check : return True

    return False


path = "+ + + ^ + + ^ ^ 1 + + ^ + ^ 2 ^ ^ ^ ^ 1 2 + ^ 2 + +"

graph_edges = [
    (1,2),
    (2,3),(2,16),(2,20),
    (3,4),(3,12),
    (4,5),(4,9),
    (5,6),(5,7),(5,8),
    (9,10),(9,11),
    (12,13),(12,14),(12,15),
    (16,17),(16,18),
    (18,19),
    (20,21),(20,22),(20,25),(20,26),
    (22,23),
    (23,24)
]

# print(my_solve(26, 1, graph_edges, path))
# print(my_solve(12, 1, [(1, 2), (2, 3), (3, 4), (4, 5), (3, 6), (3, 7), (7, 8), (3, 9), (2, 10), (1, 11), (11, 12)], "+ + + + ^ ^ + + ^ ^ + +"))



runtests(my_solve)