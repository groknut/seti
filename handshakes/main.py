import networkx as nx
import numpy as np
import matplotlib.pyplot as pp
from collections import Counter
from pathlib import Path

base = Path(__file__).parent
assets_dir = base / "assets"
assets_dir.mkdir(exist_ok=True)

G = nx.Graph()
for f in files:
    G.add_edges_from(nx.read_edgelist(f, nodetype=int).edges())

G = G.subgraph(max(nx.connected_components(G), key=len)).copy()
print(f"Вершин: {G.number_of_nodes()}, рёбер: {G.number_of_edges()}")

dist = Counter()
for u, d in nx.all_pairs_shortest_path_length(G):
    for v, l in d.items():
        if u < v:
            dist[l] += 1
total = sum(dist.values())

lengths  = sorted(dist)
counts   = [dist[l] for l in lengths]
expanded = np.repeat(lengths, counts)
mode     = max(dist, key=dist.get)
median   = np.median(expanded)
share6   = sum(c for l, c in dist.items() if l <= 6) / total

print("Расстояние | Пар | Доля")
for l in lengths:
    print(f"{l:>10} | {dist[l]:>8} | {dist[l]/total:.2%}")
print(f"Мода={mode}, Медиана={median}, Доля≤6={share6:.2%}")

fig, (ax1, ax2) = pp.subplots(1, 2, figsize=(12, 4))
ax1.bar(lengths, counts, color='steelblue', edgecolor='k')
ax1.axvline(mode, color='red', ls='--', label=f'Мода={mode}')
ax1.axvline(median, color='green', ls='--', label=f'Медиана={median}')
ax1.set(xlabel='Расстояние', ylabel='Число пар', title='Распределение')
ax1.legend()
ax2.plot(lengths, np.cumsum(counts) / total * 100, 'o-', color='orange')
ax2.axhline(50, color='gray', ls=':')
ax2.grid(alpha=.3)
ax2.set(xlabel='Расстояние', ylabel='Накопленная доля, %', title='CDF')
pp.tight_layout()
pp.savefig(assets_dir / "dist.png", dpi=120)
pp.show()
