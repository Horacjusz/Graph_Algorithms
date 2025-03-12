def solve(N, entrance, corridors, path) :
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