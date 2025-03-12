# Wierzchołek v w grafie skierowanym nazywamy tzw. dobrym początkiem,
# jeśli każdy inny wierzchołek można osiągnąć ścieżką skierowaną wychodzącą z v.
# Podać algorytm który dla podanego grafu stwierdza czy G posiada dobry początek

def good_start(G):
    V = len(G)
    def DFSvisit(G,i):
        nonlocal times, time, visited
        visited[i] = True
        for v in G[i]:
            if not visited[v]:
                DFSvisit(G,v)
        time += 1
        times[i] = time
    
    times = [None] * V
    time = 0
    visited = [False] * V
    for i in range(V):
        if not visited[i]:
            DFSvisit(G,i)
    
    
    ind = times.index(max(times))
    visited = [False] * V
    time = 0
    output = ind
    DFSvisit(G,ind)
    for v in visited :
        if not v :
            return v
    return output

G = [[1,3],[2],[],[4],[2]]


print(good_start(G))

#dobre ujście (good ending) grafu G to dobry początek dla grafu odwrotnego do G