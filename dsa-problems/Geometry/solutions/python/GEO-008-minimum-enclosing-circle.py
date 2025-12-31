import math, random
from typing import List, Tuple

def min_enclosing_circle(xs: List[int], ys: List[int]) -> Tuple[float,float,float]:
    pts = list(zip(xs, ys))
    random.shuffle(pts)

    def dist(a, b):
        dx, dy = a[0]-b[0], a[1]-b[1]
        return math.hypot(dx, dy)

    def circle_two(a, b):
        cx = (a[0]+b[0]) / 2.0
        cy = (a[1]+b[1]) / 2.0
        r = dist(a, b) / 2.0
        return (cx, cy, r)

    def circle_three(a, b, c):
        d = 2*(a[0]*(b[1]-c[1]) + b[0]*(c[1]-a[1]) + c[0]*(a[1]-b[1]))
        if abs(d) < 1e-15:
            return (0.0, 0.0, -1.0)  # invalid
        ux = ((a[0]*a[0]+a[1]*a[1])*(b[1]-c[1]) + (b[0]*b[0]+b[1]*b[1])*(c[1]-a[1]) + (c[0]*c[0]+c[1]*c[1])*(a[1]-b[1])) / d
        uy = ((a[0]*a[0]+a[1]*a[1])*(c[0]-b[0]) + (b[0]*b[0]+b[1]*b[1])*(a[0]-c[0]) + (c[0]*c[0]+c[1]*c[1])*(b[0]-a[0])) / d
        r = dist((ux, uy), a)
        return (ux, uy, r)

    def inside(p, c):
        cx, cy, r = c
        return dist(p, (cx, cy)) <= r + 1e-12

    c = (pts[0][0], pts[0][1], 0.0)
    for i in range(1, len(pts)):
        if inside(pts[i], c): continue
        c = (pts[i][0], pts[i][1], 0.0)
        for j in range(i):
            if inside(pts[j], c): continue
            c = circle_two(pts[i], pts[j])
            for k in range(j):
                if inside(pts[k], c): continue
                c = circle_three(pts[i], pts[j], pts[k])
    return c


def main() -> None:
    import sys
    sys.setrecursionlimit(200000)
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    try:
        n = int(next(it))
        xs = []
        ys = []
        for _ in range(n):
            xs.append(int(next(it)))
            ys.append(int(next(it)))
        cx, cy, r = min_enclosing_circle(xs, ys)
        if abs(r) < 1e-9: r = 0.0
        if abs(cx) < 1e-9: cx = 0.0
        if abs(cy) < 1e-9: cy = 0.0

        print(f"{cx:.6f}\n{cy:.6f}\n{r:.6f}")
    except StopIteration:
        return

if __name__ == "__main__":
    main()
