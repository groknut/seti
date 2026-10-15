import sys

def main():
    with open("input.txt") as f:
        data = f.read().split()

    it = iter(data)
    t = int(next(it))
    ans = []

    for _ in range(t):
        n = int(next(it))
        m = int(next(it))

        adj = [0] * n

        for _ in range(m):
            a = int(next(it)) - 1
            b = int(next(it)) - 1
            adj[a] |= 1 << b
            adj[b] |= 1 << a

        found = False

        for u in range(n):
            bits = adj[u]
            while bits:
                lsb = bits & -bits
                v = lsb.bit_length() - 1
                bits ^= lsb

                if v > u:
                    common = adj[u] & adj[v]
                    if common & (common - 1):
                        found = True
                        break

            if found:
                break

        ans.append("1" if found else "-1")

    print(" ".join(ans))

if __name__ == "__main__":
    main()
