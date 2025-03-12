def DFS(G) :
    V = len(G)
    times = [float('inf')] * V
    parent = [None] * V
    visited = [False] * V
    def DFSVisit(G,s) :
        nonlocal time
        time += 1
        visited[s] = True
        times[s] = time
        for v in G[s] :
            if not visited[v] :
                parent[v] = s
                DFSVisit(G,v)
        
    time = 0
    for v in range(V) :
        if not visited[v] :
            DFSVisit(G,v)
            
    print(times)




#Chyba dziala, ale i tak jest chujowe
 
def DFS_iterative(G) :
    
    V = len(G)
    visited = [False] * V
    parents = [None] * V
    visit_time = [float('inf')] * V
    
    def DFS_visit(G,u,visited,parents,visit_time) :
        
        time = 0
        
        stack = []
        stack.append([u,0])
        
        while stack :
            p,start = stack.pop()
            length = len(G[p])
            
            time += 1
            visited[p] = True
            visit_time[p] = min(visit_time[p],time)
            if visit_time[p] < time :
                time -= 1
            
            for i in range(start,length) :
                v = G[p][i]
                if not visited[v] :
                    parents[v] = p
                    stack.append([p,i + 1])
                    stack.append([v,0])
                    break
    
    consistency = 0
    for v in range(V) :
        if not visited[v] :
            consistency += 1
            DFS_visit(G,v,visited,parents,visit_time)
            
            
            




test = [[0 for _ in range(8)] for _ in range(8)]
test2 = [[] for _ in range(8)]
test3 = [[1,2],[0,4],[5,3,0],[2,4],[1,5,3],[4,2,6],[5,7],[6]]

points = [(1,2),(1,6),(1,7),(2,3),(2,7),(3,4),(3,7),(3,8),(4,5),(4,8),(5,6),(5,8),(6,7),(6,8),(7,8)]

for i in points :
    test[i[0] - 1][i[1] - 1] = 1
    test[i[1] - 1][i[0] - 1] = 1
    test2[i[0] - 1].append(i[1] - 1)
    test2[i[1] - 1].append(i[0] - 1)

DFS(test3)