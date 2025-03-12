s, t, parent):        
#     visited = [False for _ in G]
#     Q = []
#     Q.append((s,0, None))
#     while len(Q) > 0:
#         Q.sort(key=lambda x: x[1], reverse=True)
        
#         (start_node, max_flow, parent_node) = Q.pop(0)
#         if visited[start_node]:
#             continue
#         visited[start_node] = True
#         parent[start_node] = parent_node
#         for edge in G[start_node]:
#             end_node, flow_forward, _ = edge
#             if not visited[end_node] and flow_forward > 0:
#                 parent[end_node] = start_node
#                 Q.append((end_node, min(max_flow, flow_forward), start_node))
        
#         if start_node == T:
#             break
#     return visited[t]
        