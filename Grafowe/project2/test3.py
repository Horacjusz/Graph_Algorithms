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
    
    print("A = ",graph)
    print("B = ",G)
    
    if G_edges_count > graph_edges_count or V_G > N : return False
    
    G_tree,G_depth = dfs_tree(G,0,True)
    print(G_tree,G_depth)
    
    print(dfs_tree(graph,12,maximum = G_depth))
    
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

print(my_solve(26, 1, graph_edges, path))