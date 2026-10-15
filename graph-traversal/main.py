from collections import deque


def main():
    with open("graph.txt") as f:
        data = f.read().split()
    it = iter(data)
    n, k = int(next(it)), int(next(it)) - 1
    g = [[int(next(it)) for _ in range(n)] for _ in range(n)]

    dist = [-1] * n
    dist[k] = 0
    q = deque([k])

    def bfs():
        if not q:
            return
        v = q.popleft()
        for u in range(n):
            if g[v][u] and dist[u] < 0:
                dist[u] = dist[v] + 1
                q.append(u)
        bfs()

    bfs()
    for i in range(n):
        print(i + 1, dist[i])

main()
