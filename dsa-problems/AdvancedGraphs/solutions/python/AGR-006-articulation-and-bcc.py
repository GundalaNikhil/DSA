import sys

# Increase recursion depth
sys.setrecursionlimit(300000)

def articulation_and_bcc(n: int, edges: list[tuple[int, int]]):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    tin = [-1] * n
    low = [-1] * n
    timer = 0
    aps = set()
    bccs = []
    stack = []

    def dfs(u, p):
        nonlocal timer
        tin[u] = low[u] = timer
        timer += 1
        children = 0

        for v in adj[u]:
            if v == p:
                continue

            if tin[v] != -1:
                low[u] = min(low[u], tin[v])
                if tin[v] < tin[u]: # Back-edge
                    stack.append((u, v))
            else:
                stack.append((u, v))
                children += 1
                dfs(v, u)
                low[u] = min(low[u], low[v])

                if (p != -1 and low[v] >= tin[u]) or (p == -1 and children > 1):
                    aps.add(u)

                if low[v] >= tin[u]:
                    bcc = set()
                    while stack:
                        edge = stack.pop()
                        bcc.add(edge[0])
                        bcc.add(edge[1])
                        if edge == (u, v):
                            break
                    bccs.append(list(bcc))

    for i in range(n):
        if tin[i] == -1:
            dfs(i, -1)
            if stack: # Should be empty if logic is correct, but for safety
                bcc = set()
                while stack:
                    edge = stack.pop()
                    bcc.add(edge[0])
                    bcc.add(edge[1])
                if bcc:
                    bccs.append(list(bcc))

    return sorted(list(aps)), bccs

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append((u, v))

        aps, bccs = articulation_and_bcc(n, edges)

        out = [str(len(aps))]
        if aps:
            out.append(" ".join(map(str, aps)))
        
        out.append(str(len(bccs)))
        for b in bccs:
            b.sort()
            out.append(f"{len(b)} " + " ".join(map(str, b)))

        sys.stdout.write("\n".join(out).strip())
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
