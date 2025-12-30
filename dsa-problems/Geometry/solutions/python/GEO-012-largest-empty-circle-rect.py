import math
from typing import List, Tuple

EPS = 1e-12

def largest_empty_circle(xL: int, yB: int, xR: int, yT: int, xs: List[int], ys: List[int]) -> float:
    pts = list(zip(xs, ys))
    n = len(pts)

    def inside_rect(p):
        return xL - EPS <= p[0] <= xR + EPS and yB - EPS <= p[1] <= yT + EPS

    def dist_to_edge(p):
        return min(p[0]-xL, xR-p[0], p[1]-yB, yT-p[1])

    def dist(p, q):
        return math.hypot(p[0]-q[0], p[1]-q[1])

    cand = []
    # rectangle corners
    cand.extend([(xL, yB), (xL, yT), (xR, yB), (xR, yT)])
    # edge projections of points
    for x, y in pts:
        cand.append((x, yB)); cand.append((x, yT))
        cand.append((xL, y)); cand.append((xR, y))
    # midpoints of pairs
    for i in range(n):
        for j in range(i+1, n):
            mx = (pts[i][0]+pts[j][0])/2.0
            my = (pts[i][1]+pts[j][1])/2.0
            cand.append((mx, my))
    # circumcenters for small n
    if n <= 60:
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    ax, ay = pts[i]; bx, by = pts[j]; cx, cy = pts[k]
                    d = 2*(ax*(by-cy) + bx*(cy-ay) + cx*(ay-by))
                    if abs(d) < EPS: continue
                    ux = ((ax*ax+ay*ay)*(by-cy) + (bx*bx+by*by)*(cy-ay) + (cx*cx+cy*cy)*(ay-by)) / d
                    uy = ((ax*ax+ay*ay)*(cx-bx) + (bx*bx+by*by)*(ax-cx) + (cx*cx+cy*cy)*(bx-ax)) / d
                    cand.append((ux, uy))

    best = 0.0
    for p in cand:
        if not inside_rect(p): continue
        d_edge = dist_to_edge(p)
        d_pt = float('inf')
        for q in pts:
            d_pt = min(d_pt, dist(p, q))
        r = min(d_edge, d_pt)
        if r > best: best = r
    return best

if __name__ == "__main__":
    main()
