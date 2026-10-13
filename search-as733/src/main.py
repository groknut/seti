import networkx as nx

with open('data/as20000102.txt') as f:
    lines = [l for l in f if l.strip() and not l.lstrip().startswith('#')]

G = nx.parse_edgelist(lines, nodetype=int)
d = dict(G.degree())

for u in G:
    if d[u] < 10: continue
    for v in G:
        if u < v and d[v] >= 10 and not G.has_edge(u, v):
            print(u, v, d[u], d[v])
            exit()
