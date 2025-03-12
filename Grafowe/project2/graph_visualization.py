from dimacs import *
import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph_list):
    G = nx.Graph()
    for index, neighbors in enumerate(graph_list):
        for neighbor in neighbors:
            G.add_edge(index, neighbor)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.show()


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

def both(N, entrance, corridors, path):
    
    G = [[] for _ in range(N)]
    G_edges_count = 0
    for corridor in corridors :
        if corridor[0] == entrance or corridor[1] == entrance : continue
        G_edges_count += 1
        G[corridor[0] - 1].append(corridor[1] - 1)
        G[corridor[1] - 1].append(corridor[0] - 1)
    
    path_steps = []
    V_graph = 1
    for step in path :
        if step == "+" : V_graph += 1
    path_steps = path.split(" ")


    path_graph = [[] for _ in range(V_graph)]

    path_parents = [None for _ in range(V_graph)]

    placeholder = 0
    current = 0

    for step in path_steps :
        if step == "+" :
            current += 1
            
            path_parents[current] = placeholder
            path_graph[placeholder].append(current)
            path_graph[current].append(placeholder)
            placeholder = current
            
        elif step == "^" :
            
            placeholder = path_parents[placeholder]
            
        else :
            st = int(step)
            if placeholder == 0 : st -= 1
            placeholder = path_graph[placeholder][st]
            
    return G,path_graph

def graphs(name, entrance = 0) :
    V,edges,path,solution = reading(name)
    
    A,B = both(V,entrance,edges,path)
    
    visualize_graph(A)
    visualize_graph(B)
    
graphs("maze-3d-med")