from random import randint

def rand_graph_create(V,E,directed = False) :
    if 2*E > V*(V-1) :
        return
    G = [[] for _ in range(V)]
    edges = 0
    while edges < E :
        start = randint(0,V - 1)
        end = randint(0,V - 1)
        
        if start == end :
            continue
        
        if end in G[start] :
                continue
        
        if directed :
            G[start].append(end)
        if not directed :
            G[start].append(end)
            G[end].append(start)
        edges += 1

    return G
print(rand_graph_create(8,14,True))