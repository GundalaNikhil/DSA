def components(n: int, adj: list[list[int]]) -> list[int]:
    comp = [0] * n
    count = 0
    stack = []

    for i in range(n):
        if comp[i] != 0:
            continue
        count += 1
        stack.append(i)
        comp[i] = count
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if comp[v] == 0:
                    comp[v] = count
                    stack.append(v)
    return comp

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    comp = components(n, adj)
    max_comp = max(comp) if comp else 0
    sys.stdout.write(str(max_comp))

if __name__ == "__main__":
    main()
