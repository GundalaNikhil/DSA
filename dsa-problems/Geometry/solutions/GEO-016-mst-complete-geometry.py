def manhattan_mst(xs, ys):
    n = len(xs)
    pts = [(xs[i], ys[i], i) for i in range(n)]
    edges = []
    def add_edges(transform):
        arr = [transform(x,y,i) for x,y,i in pts]
        arr.sort()
        best = {}
        for tx, ty, ox, oy, idx in arr:
            key = ty - tx
            if key in best:
                j = best[key][1]
                w = abs(ox - pts[j][0]) + abs(oy - pts[j][1])
                edges.append((w, idx, j))
            val = tx + ty
            if key not in best or val > best[key][0]:
                best[key] = (val, idx)
    add_edges(lambda x,y,i:(x, y, x, y, i))
    add_edges(lambda x,y,i:(-x, y, x, y, i))
    add_edges(lambda x,y,i:(x, -y, x, y, i))
    add_edges(lambda x,y,i:(-x, -y, x, y, i))
    # Kruskal
    parent=list(range(n)); rank=[0]*n
    def find(a):
        while a!=parent[a]:
            parent[a]=parent[parent[a]]; a=parent[a]
        return a
    def union(a,b):
        a=find(a); b=find(b)
        if a==b: return False
        if rank[a]<rank[b]: a,b=b,a
        parent[b]=a
        if rank[a]==rank[b]: rank[a]+=1
        return True
    edges = list(set(edges))
    edges.sort()
    ans=0; cnt=0
    for w,u,v in edges:
        if union(u,v):
            ans+=w; cnt+=1
            if cnt==n-1: break
    return ans


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
