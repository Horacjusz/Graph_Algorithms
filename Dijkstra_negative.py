from queue import PriorityQueue

def dijkstra_negative(G,s,t,directed = False):
    V = len(G)
    infinity = float('inf')
    distances = [infinity for _ in range(V)]
    distances[s] = 0
    visited = [[False for _ in range(V)] for _ in range(V)]
    Q = PriorityQueue()
    Q.put((0,s))
    output = infinity
    
    while not Q.empty() :
        dist,v = Q.get()
        if v == t :
            output = dist
            break
        for n,val in G[v] :
            if visited[v][n] :
                continue
            if distances[n] > dist + val :
                distances[n] = dist + val
                Q.put((distances[n],n))
                visited[v][n] = True
                if not directed :
                    visited[n][v] = True
    print(distances)
    if output == infinity :
        return None
    
    return output

test = [[(1,3),(2,4)],[(0,3),(4,3)],[(5,1),(3,3),(0,4)],[(2,3),(4,5)],[(1,3),(5,2),(3,5)],[(4,2),(2,1),(6,3)],[(5,3),(7,-6)],[(6,-6)]]

print(dijkstra_negative(test,0,7))