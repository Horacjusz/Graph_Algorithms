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


def is_subtree_of(A,B,a,b) :
    A_parents = [None]*len(A)
    B_parents = [None]*len(B)
    
    
    b_checked = [[] for _ in range(len(B))]

    def check_subtree(a,b,level = 0) :
        nonlocal A, B, A_parents, B_parents, b_checked
        
        header = ''
        for _ in range(level) :
            header += "-"
        header += ">"
        
        if len(B[b]) > len(A[a]) : return False
        
        occupied = []
        pairs = []
        
        b_stack = []
        for b_child in B[b] :
            if b_child == B_parents[b] : continue
            b_stack.append(b_child)
        
        
        while b_stack :
            b_child = b_stack.pop()
            if b_child == B_parents[b] : continue
            B_parents[b_child] = b
            match_found = False
            for a_child in A[a] :
                if a_child == A_parents[a] : continue
                if a_child in occupied : continue
                A_parents[a_child] = a
                if check_subtree(a_child,b_child,level = level+1) :
                    # print(header,b,a,"->",b_child,a_child)
                    occupied.append(a_child)
                    pairs.append((b_child,a_child))
                    match_found = True
                    break
            
            if not match_found :
                for i in range(len(pairs)) :
                    b_s,a_s = pairs[i]
                    if b_s in b_checked[b_child] : continue
                    if check_subtree(a_s,b_child,level = level+1) :
                        b_checked[b_child].append(b_s)
                        b_stack.append(b_s)
                        match_found = True
                        break
                
            if not match_found : return False
        
        
        
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
    
    if G_edges_count > graph_edges_count or V_G > N : return False
    

    for v in range(N) :
        if v == entrance - 1 : continue
        if is_subtree_of(graph, G, v, 0) : return True
    
    return False



runtests(my_solve)
