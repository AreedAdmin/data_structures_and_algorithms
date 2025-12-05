marked = [False] * len(G)
#DFS Recursive
#dfs recursive pre order traversal
marked = [False] * len(G)
def dfs_pre(G,v):
    visit(v)
    marked[v] = True
    for w in G.neighbors(v):
        if not marked[w]:
        dfs_pre(G,w)

#dfs recursive post order traversal
marked = [False] * len(G)
def dfs_post(G,v):
    marked[v] = True
    for w in G.neighbors(v):
        if not marked[w]:
            dfs_post(G,w)
    visit(v)