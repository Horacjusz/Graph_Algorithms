from collections import deque

def BFS(G, s, t ):
    V = len(G)
    visited = [False for _ in range(V)]
    parent = [None for _ in range(V)]
    distances = [0 for _ in range(V)]
    Q = deque()
    Q.append(s)
    visited[s] = True
    breaking = False
    while Q :
        v = Q.popleft()
        dist = distances[v] + 1
        for n in G[v] :

            if visited[n]:
                continue
            visited[n] = True
            distances[n] = dist
            parent[n] = v
            if n == t :
                breaking = True
                break
            Q.append(n)
        if breaking :
            break
    path = [t]
    c = parent[t]
    while c is not None :
        path = [c] + path
        c = parent[c]
    
    return distances

    

test = [[0 for _ in range(8)] for _ in range(8)]
test2 = [[] for _ in range(8)]
test3 = [[1,2],[0,4],[5,3,0],[2,4],[1,5,3],[4,2,6],[5,7],[6]]

points = [[1,2],[1,6],[1,7],[2,3],[2,7],[3,4],[3,7],[3,8],[4,5],[4,8],[5,6],[5,8],[6,7],[6,8],[7,8]]

for i in points :
    i[0] -= 1
    i[1] -= 1
    test[i[0]][i[1]] = 1
    test[i[1]][i[0]] = 1
    test2[i[0]].append(i[1])
    test2[i[1]].append(i[0])

print(test3)
for i in range(len(test3)) :
    print(test3[i])

test4 = [[1, 2], [0, 3], [0, 4], [1, 5, 6], [2, 7], [3, 8], [3, 8], [4, 8], [5, 6, 7, 9], [8, 10, 11], [9, 12], [9, 12], [10, 11]]
#s :  0 t :  12 Mozliwe wyniki  :  [(8, 9)]
print()
print(BFS(test4,0,12))