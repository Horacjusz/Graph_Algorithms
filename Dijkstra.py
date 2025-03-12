from random import randint
import heapq

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
            if distance < distances[n]:
                distances[n] = distance
                parents[n] = v
                heapq.heappush(Q, (distance, n))
    print(parents)
    return distances

test_graph = [[[1, 3]], [[0, 3], [2, 5], [3, 3]], [[1, 5], [3, 1], [4, 6]], [[1, 3], [2, 1], [4, 9]], [[2, 6], [3, 9], [5, 1], [6, 8], [9, 7], [14, 3]], [[4, 1], [6, 8]], [[4, 8], [5, 1], [7, 5], [8, 11]], [[6, 5], [8, 7]], [[7, 7], [6, 11]], [[4, 7], [10, 3], [14, 8]], [[9, 3], [11, 13], [14, 2]], [[10, 13], [12, 5], [13, 2]], [[11, 5], [13, 2]], [[11, 2], [12, 2]], [[4, 3], [9, 8], [10, 2], [15, 7], [16, 7]], [[14, 7], [16, 4], [17, 5]], [[14, 7], [15, 4], [17, 6]], [[15, 5], [16, 6], [18, 13]], [[17, 13]]]
print(dijkstra(test_graph,1))

# def dijkstra_matrix(G,s) :
#     V = len(G)
#     parents = [None for _ in range(V)]
#     distances = [float('inf')] * V
#     distances[s] = 0
    
#     Q = [(0,s)]
    
#     while Q :
#         _, v = heapq.heappop(Q)
#         dist = distances[v]
        
#         for n in range(V) :
#             val = G[v][n]
#             if val == -1 :
#                 continue
#             if n == parents[v] :
#                 continue
            
#             distance = dist + val
#             if distance < distances[n]:
#                 distances[n] = distance
#                 parents[n] = v
#                 heapq.heappush(Q, (-distance, n))
#     print(parents)
#     return distances

# def rand_weighted_graph(V = 8,E = 10, max_weight = 10, neg_weight = False ,directed = False) :
#     if 2*E > V*(V-1) :
#         return
#     G = [[] for _ in range(V)]
#     edges = 0
#     while edges < E :
#         start = randint(0,V - 1)
#         end = randint(0,V - 1)
#         if start == end :
#             continue
#         continuity = False
#         for i in G[start] :
#             if i[0] == end :
#                 continuity = True
#                 break
#         if continuity :
#             continue
            
#         weight = 0
#         if neg_weight :
#             weight = randint(-max_weight,max_weight)
#         else :
#             weight = randint(0,max_weight)
            
#         if directed :
#             G[start].append((end, weight))
#         if not directed :
#             G[start].append((end, weight))
#             G[end].append((start,weight))
        
#         edges += 1

#     for i in range(V) :
#         G[i] = sorted(G[i])

#     return G

# def list_to_matrix(G,stopper = -1) :
#     V = len(G)
#     D = [[stopper for j in range(V)] for _ in range(V)]
    
#     for v in range(V) :
#         for n,val in G[v] :
#             D[v][n] = val
#             D[v][n] = val
    
#     for _ in D :
#         print(_)
#     print()
#     return D
    
        

# #G = rand_weighted_graph()
# G = [[(3, 10), (5, 8), (6, 10)], [(3, 6)], [(6, 7)], [(0, 10), (1, 6), (4, 10), (5, 8), (6, 7)], [(3, 10), (7, 6)], [(0, 8), (3, 8), (6, 4)], [(0, 10), (2, 7), (3, 7), (5, 4)], [(4, 6)]]

# for _ in G :
#     print(_)
# #G2 = list_to_matrix(G)

# #for i in G :
# #    print(i)
    
# print()
# print(dijkstra(G,0))
# #print(dijkstra_matrix(G2,0))
# #print()
# #print(G2)