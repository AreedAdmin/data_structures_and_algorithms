marked = [False] * len(G)
def dfs_iter(G,v):
    stack = [v]
    
    while len(stack) > 0:
        v = stack.pop()

        if not marked[v]:
            marked[v] = True
            for w in G.neighbors(v):
                stack.append(w)
    return marked