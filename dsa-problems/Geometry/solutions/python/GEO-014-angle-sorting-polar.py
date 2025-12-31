import functools
def sort_by_angle(xs, ys):
    pts = list(zip(xs, ys))
    def half(p):
        x,y = p
        return 0 if (y > 0 or (y == 0 and x > 0)) else 1
    def cmp(a, b):
        ha, hb = half(a), half(b)
        if ha != hb:
            return -1 if ha < hb else 1
        cross = a[0]*b[1] - a[1]*b[0]
        if cross != 0:
            return -1 if cross > 0 else 1
        ra = a[0]*a[0] + a[1]*a[1]
        rb = b[0]*b[0] + b[1]*b[1]
        if ra == rb: return 0
        return -1 if ra < rb else 1
    pts.sort(key=functools.cmp_to_key(cmp))
    return pts

def main() -> None:
    import sys
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    try:
        n = next(it)
        xs = []
        ys = []
        for _ in range(n):
            xs.append(next(it))
            ys.append(next(it))
        res = sort_by_angle(xs, ys)
        for x, y in res:
            print(f"{x} {y}")
    except StopIteration:
        return

if __name__ == "__main__":
    main()
