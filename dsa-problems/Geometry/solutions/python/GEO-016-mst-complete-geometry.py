def manhattan_mst(xs, ys):
    import sys
    n = len(xs)
    if n <= 1:
        return 0

    points = []
    for i in range(n):
        points.append([xs[i], ys[i], i])

    edges = []

    def build_edges():
        # Sort by x then y
        points.sort()
        
        # Coordinate compression for y - x
        coords = sorted(list(set(p[1] - p[0] for p in points)))
        rank = {val: i + 1 for i, val in enumerate(coords)}
        m = len(coords)
        
        # BIT to store (min_val, point_id)
        # We want to find point j with yj - xj >= yi - xi that minimizes xj + yj
        bit = [(float('inf'), -1)] * (m + 1)

        def update(idx, val, pid):
            while idx > 0:
                if val < bit[idx][0]:
                    bit[idx] = (val, pid)
                idx -= idx & -idx

        def query(idx):
            res = (float('inf'), -1)
            while idx <= m:
                if bit[idx][0] < res[0]:
                    res = bit[idx]
                idx += idx & -idx
            return res

        for i in range(n - 1, -1, -1):
            cur_p = points[i]
            x, y, pid = cur_p
            r = rank[y - x]
            res_val, res_pid = query(r)
            if res_pid != -1:
                dist = abs(xs[pid] - xs[res_pid]) + abs(ys[pid] - ys[res_pid])
                edges.append((dist, pid, res_pid))
            update(r, x + y, pid)

    # 4 transformations
    for _ in range(2):
        for _ in range(2):
            build_edges()
            # Swap x and y
            for p in points:
                p[0], p[1] = p[1], p[0]
        # Negate y
        for i in range(n):
            points[i][1] = -points[i][1]

    # Kruskal's
    edges.sort()
    parent = list(range(n))
    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    mst_weight = 0
    num_edges = 0
    for d, u, v in edges:
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            parent[root_u] = root_v
            mst_weight += d
            num_edges += 1
            if num_edges == n - 1:
                break
    return mst_weight

def main() -> None:
    import sys
    # Use robust reading for large inputs
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        xs = []
        ys = []
        for _ in range(n):
            xs.append(int(next(it)))
            ys.append(int(next(it)))
        print(manhattan_mst(xs, ys))
    except StopIteration:
        return

if __name__ == "__main__":
    main()
