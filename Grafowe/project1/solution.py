# Paweł Prus
# Na chwile obecną złożoność obliczniowa programu wynosi w najbardziej pesymistycznym ujęciu O(EV)
# Jednakże optymistycznie wynosi ona O(ElogV).
# Obecnie program ma jeszce problem z przerzucaniem klik przy tworzeniu nowego drzewa, co powoduje błędne wyniki w cześci testów
# Da się to naprawić, a jednocześnie zmniejszyć złożoność tworząc ścieżki równolegle z Dijkstrą



from data import runtests
import heapq
from collections import deque
from copy import deepcopy

def articulation_points(G) :
    V = len(G)
    times = [0] * V
    parent = [None] * V
    visited = [False] * V
    low = [0] * V
    
    articulations = []
    def DFSVisit(G,s) :
        nonlocal time,low,visited,articulations,parent
        
        no_children = 0
        
        visited[s] = True
        times[s] = time
        low[s] = time
        time += 1
        for v in G[s] :
            if not visited[v] :
                parent[v] = s
                no_children += 1
                DFSVisit(G,v)
                low[s] = min(low[s],low[v])
                if parent[s] is None and no_children > 1 :
                    articulations.append(s)
                if parent[s] is not None and low[v] >= times[s] :
                    articulations.append(s)
            elif v != parent[s] :
                low[s] = min(low[s],times[v])  
       
    time = 0
    for v in range(V) :
        if not visited[v] :
            DFSVisit(G,v)
    if len(articulations) == 0 : return []
    if len(articulations) == 1 : return articulations
    
    articulations.sort()
    for i in range(len(articulations) - 2,-1,-1) :
        if articulations[i] == articulations[i+1] : articulations.pop(i+1)
    
    return articulations



def spec_dijkstra(G,s,arts,data,indexes,checked,first = False) :
    V = len(G)
    parents = [None for _ in range(V)]
    distances = [float('inf')] * V
    distances[s] = 0
    
    done = [False]*V
    done[s] = True
    
    Q = [(0,s)]
    
    output = []
    while Q :
        _, v = heapq.heappop(Q)
        dist = distances[v]
        
        # print(v,G[v])
        
        for n,val in G[v] :
            if n == parents[v] :
                continue
            if not first and checked[n] :
                continue
            
            if s not in data[n] :
                continue
            
            distance = dist + val
            if distance < distances[n] :
                distances[n] = distance
                if arts[v] : parents[n] = v
                else :
                    parents[n] = parents[v]

                heapq.heappush(Q, (distance, n))
    
    # print(distances)
          
    for i in range(V) :
        if distances[i] != float('inf') :
            checked[i] = True
    for i in range(V) :
        dist = distances[i]
        if dist == float('inf') : continue
        if arts[i] and i != s : 
            output.append((indexes[i],dist))
            if parents[i] != s :
                t = i
                while not done[t] :
                    t = parents[t]
                    output.append((indexes[i],indexes[t],dist - distances[t]))
                    done[t] = True
                    
    min_w = float('inf')
    point = None
    for n,w in G[s] :
        if len(data[n]) == 1 :
            if w < min_w :
                min_w = w
                point = n
    if point is not None :
        output.append((indexes[point],min_w))
    points = 0
    for art in arts :
        if art :
            points += 1
    
    if points == 1 :
        min_w = float('inf')
        point2 = None
        for n,w in G[s] :
            if len(data[n]) == 1 and n != point :
                if w < min_w:
                    min_w = w
                    point2 = n
        if point2 is not None :
            output.append((indexes[point2],min_w))
    
    return output

def spec_BFS(G, s, arts, data ) :
    V = len(G)
    visited = [False for _ in range(V)]
    parent = [None for _ in range(V)]
    distances = [0 for _ in range(V)]
    Q = deque()
    Q.append(s)
    visited[s] = True
    while Q :
        v = Q.popleft()
        dist = distances[v] + 1
        for n in G[v] :
            if visited[n] or len(data[n]) > 1 : continue
            visited[n] = True
            distances[n] = dist
            parent[n] = v
            data[n].append(s)
            if not arts[n] :
                Q.append(n)
    
    return data

def BFS(G, s) : 
    V = len(G)
    visited = [False for _ in range(V)]
    parent = [None for _ in range(V)]
    distances = [0 for _ in range(V)]
    Q = deque()
    Q.append(s)
    visited[s] = True
    paths = [None]*V
    paths[s] = [s]
    while Q :
        v = Q.popleft()
        dist = distances[v]
        curr_path = deepcopy(paths[v])
        for n,w in G[v] :
            if visited[n] : continue
            path = deepcopy(curr_path)
            path.append(n)
            paths[n] = path
            visited[n] = True
            distances[n] = dist + w
            parent[n] = v
            Q.append(n)
    
    # print(paths)
    output = []
    for path in paths :
        if path is not None :
            # print(G[path[-1]])
            if len(G[path[-1]]) <= 1 and len(path) > 1 :
                # print('stepped')
                output.append(path)
    # print("output",output)
    return output
    
def dijkstra(G,s) :
    V = len(G)
    parents = [None for _ in range(V)]
    distances = [float('inf')] * V
    distances[s] = 0
    
    Q = [(0,s)]
    
    while Q :
        _, v = heapq.heappop(Q)
        dist = distances[v]
        
        for n,val in G[v] :
            if n == parents[v] :
                continue
            
            distance = dist + val
            if distance < distances[n] :
                distances[n] = distance
                parents[n] = v
                heapq.heappush(Q, (distance, n))
    
    return distances

def G_seek(G,v,s) :
    for n,w in G[v] :
        if n == s : return w
        
def path_val(path,G) :
    if len(path) == 1 : return (0,0)
    value = 0
    for i in range(1,len(path)) :
        value += G_seek(G,path[i-1],path[i])
    return value


def solution(graph) :
    V1 = len(graph)
    graph_no_weight = [[] for _ in range(V1)]
    for v in range(V1) :
        for n,_ in graph[v] :
            graph_no_weight[v].append(n)
        
    articulation = articulation_points(graph_no_weight)
    articulation.sort()
    for i in range(len(articulation)) :
        articulation[i] += 1
    for i in range(len(articulation)) :
        articulation[i] -= 1
    arts = [False]*V1
    for i in range(len(articulation)) :
        arts[articulation[i]] = True
        
    V = len(articulation)
    data = [[] for _ in range(V1)]
    
    for a in articulation :
        data = spec_BFS(graph_no_weight,a,arts,data)

    indexes = [None]*V1
    for i in range(len(articulation)) :
        indexes[articulation[i]] = i
    leaves = 0
    for i in range(len(data)) :
        if len(data[i]) == 1 : 
            indexes[i] = V + leaves
            leaves += 1
    V += leaves
    
    
    checked = [False]*V1
    
    checked = [False]*V1
    V2 = len(articulation)
    G = [[] for _ in range(V)]
    for a in articulation :
        check = False
        if indexes[a] == 0 : check = True
        new = spec_dijkstra(graph,a,arts,data,indexes,checked,check)
    
        for record in new :
            if len(record) == 2 :
                G[indexes[a]].append(record)
                G[record[0]].append((indexes[a],record[1]))
            if len(record) == 3 :
                G[record[0]].append((record[1],record[2]))
                G[record[1]].append((record[0],record[2]))
                
    # print("GRAPH")
    # for _ in G :
    #     print(_)
    # print()
    
    G_no_weight = [[] for _ in range(V)]
    for v in range(V) :
        for n,_ in G[v] :
            G_no_weight[v].append(n)
    
    paths = [[None for _ in range(leaves)] for _ in range(leaves)]
    V2 = len(articulation)
    for i in range(V2,V) :
        if G[i] == None :
            continue
        curr_paths = BFS(G,i)
        paths[i - V2] = curr_paths
        
    # for i in range(V2,V) :
    #     print(i,paths[i - V2])
    

    max_length = float('-inf')
    for current in paths :
        for path in current :
            if path is None : continue
            if len(path) > max_length :
                max_length = len(path)
    
    maxes = []
    for current in paths :
        for path in current :
            if path is None : continue
            if len(path) == max_length :
                maxes.append(path)
    
    shortest = float('inf')
    # end_path = None
    for path in maxes :
        val = path_val(path,G)
        if val < shortest :
            shortest = val
            # end_path = path
    # print(end_path)
    return max_length - 2,shortest
    

    # shortest = float('inf')
    # for current in paths :
    #     for path in current :
    #         val = path_val(path,G)
    #         if val < shortest :
    #             shortest = val
    
    # mins = []            
    # for current in paths :
    #     for path in current :
    #         val = path_val(path,G)
    #         if val == shortest :
    #             mins.append(path)
    
    # longest = float('-inf')
    # for path in mins :
    #     if len(path) > longest :
    #         longest = len(path)
    
    # return longest - 2, shortest
    
            
    


def my_solve(N, streets):
    # print(f"Place: {N}, ulice: {len(streets)}")
    G = [[] for _ in range(N)]
    for a, b, t in streets:
        G[a - 1].append((b - 1,t))
        G[b - 1].append((a - 1,t))
    output = solution(G)
    
    
    
    return output

# runtests(my_solve)



problems = [

# Optimal path: 1 2 3
{"arg": [3, [
    (1, 2, 2),
    (2, 3, 5),
  ]],
  "hint": (1, 7)},


# Optimal path: 1 3 4
{"arg": [4, [
  (3, 1, 2),
  (3, 2, 4),
  (3, 4, 1),
  ]],
  "hint": (1, 3)},


# Optimal path: 1 3 4 5
{"arg": [6, [
  (1, 3, 1),
  (2, 3, 2),
  (3, 4, 5),
  (4, 5, 1),
  (4, 6, 3),
  ]],
  "hint": (2, 7)},


# Optimal path: 4 1 3 2 5
{"arg": [6, [
  (1, 2, 3),
  (2, 3, 1),
  (1, 3, 1),
  (1, 4, 1),
  (3, 6, 8),
  (2, 5, 3),
  ]],
  "hint": (2, 6)},


# Optimal path: 2 1 3
{"arg": [6, [
  (1, 2, 2),
  (1, 3, 3),
  (1, 4, 4),
  (1, 5, 5),
  (1, 6, 6),
  ]],
  "hint": (1, 5)},


# Optimal path: 2 1 3 etc
{"arg": [6, [
  (1, 2, 1),
  (1, 3, 2),
  (1, 4, 2),
  (1, 5, 2),
  (1, 6, 2),
  ]],
  "hint": (1, 3)},


# Optimal path: 1 2 3 4 6
{"arg": [7, [
  (1, 2, 2),
  (2, 3, 3),
  (3, 4, 5),
  (4, 6, 1),
  (4, 5, 2),
  (4, 7, 3),
  ]],
  "hint": (3, 11)},


# Optimal path: 13 4 11 1 8 3 10
{"arg": [13, [
  (1, 5, 3),
  (1, 6, 8),
  (5, 6, 1),
  (5, 2, 5),
  (6, 2, 2),
  (2, 7, 3),
  (1, 8, 4),
  (1, 9, 3),
  (8, 9, 5),
  (8, 3, 1),
  (9, 3, 7),
  (3, 10, 2),
  (1, 11, 3),
  (1, 12, 2),
  (11, 12, 4),
  (11, 4, 1),
  (12, 4, 6),
  (4, 13, 2),
  ]],
  "hint": (3, 13)},


# Optimal path: 7 2 4 3 8
{"arg": [10, [
  (1, 2, 2),
  (1, 3, 3),
  (1, 4, 2),
  (1, 5, 6),
  (2, 3, 3),
  (2, 4, 1),
  (2, 5, 1),
  (3, 4, 1),
  (3, 5, 1),
  (4, 5, 4),
  (1, 6, 7),
  (2, 7, 4),
  (3, 8, 3),
  (4, 9, 5),
  (5, 10, 6),
  ]],
  "hint": (2, 9)},


# Optimal path: 14 13 11 12 4 3 2 6
{"arg": [16, [
  (1, 2, 2),
  (2, 3, 2),
  (3, 4, 1),
  (4, 5, 4),
  (5, 1, 1),
  (4, 2, 8),
  (2, 6, 3),
  (6, 7, 8),
  (2, 7, 9),
  (3, 15, 7),
  (3, 16, 9),
  (4, 8, 8),
  (8, 9, 2),
  (8, 10, 1),
  (9, 10, 5),
  (4, 11, 6),
  (4, 12, 2),
  (11, 12, 1),
  (11, 13, 1),
  (12, 13, 5),
  (13, 14, 3),
  ]],
  "hint": (3, 13)},


# Optimal path: 14 12 11 15 5 6 7 8
{"arg": [19, [
  (1,2, 3),
  (2,3, 5), (3,4, 1), (2,4, 3), (3,5, 6), (4,5, 9),
  (5,6, 1), (6,7, 5), (5,7, 8),
  (7,8, 5), (7,9, 11), (8,9, 7),
  (5,10, 7), (10,11, 3), (11,15, 2), (5,15, 3), (10,15, 8),
  (11,12, 13),
  (12,13, 5), (13,14, 2), (12,14, 2),
  (15,16, 7), (15,17, 7), (16,17, 4), (16,18, 5), (17,18, 6),
  (18,19, 13)
  ]],
  "hint": (4, 31)},


# Optimal path: 3 2 1 28 29 30
{"arg": [37, [
  (1, 27, 7),
  (1, 28, 6),
  (1, 11, 8),
  (1, 6, 5),
  (1, 2, 4),
  (2, 7, 8),
  (2, 6, 4),
  (2, 4, 6),
  (2, 3, 2),
  (3, 5, 7),
  (3, 4, 3),
  (4, 5, 4),
  (6, 7, 4),
  (7, 9, 4),
  (7, 8, 5),
  (8, 10, 2),
  (8, 9, 3),
  (9, 10, 3),
  (11, 28, 8),
  (11, 27, 7),
  (11, 25, 2),
  (11, 21, 4),
  (11, 19, 3),
  (11, 20, 6),
  (11, 18, 5),
  (11, 16, 2),
  (11, 17, 5),
  (11, 15, 7),
  (11, 13, 4),
  (11, 14, 8),
  (11, 12, 5),
  (12, 14, 8),
  (12, 13, 3),
  (15, 17, 5),
  (15, 16, 3),
  (18, 20, 2),
  (18, 19, 8),
  (21, 26, 4),
  (21, 25, 5),
  (21, 23, 8),
  (21, 24, 5),
  (21, 22, 8),
  (22, 24, 6),
  (22, 23, 3),
  (25, 26, 4),
  (28, 36, 5),
  (28, 35, 6),
  (28, 33, 2),
  (28, 29, 4),
  (29, 34, 3),
  (29, 33, 4),
  (29, 31, 7),
  (29, 30, 3),
  (30, 32, 6),
  (30, 31, 4),
  (31, 32, 4),
  (33, 34, 6),
  (35, 37, 4),
  (35, 36, 5),
  (36, 37, 2),
  ]],
"hint": (4, 19)},
]

print(len(problems))

# for problem in problems :
#     # print(problem)
#     N = problem["arg"][0]
#     streets = problem["arg"][1]
#     sol = problem['hint']
#     print(problems.index(problem),my_solve(N,streets),sol)


problem = problems[8]

N = problem["arg"][0]
streets = problem["arg"][1]
sol = problem['hint']
print(my_solve(N,streets),sol)