import math
from typing import List, Tuple

def capped_hull(xs: List[int], ys: List[int], theta: int) -> List[Tuple[int, int]]:
    pts = sorted(set(zip(xs, ys)))
    if len(pts) == 1:
        return pts

    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

    # Monotone chain
    lower = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    hull = lower[:-1] + upper[:-1]
    h = len(hull)
    if h <= 2:
        return hull

    cosT = math.cos(math.radians(theta))
    keep = []
    for i in range(h):
        prev = hull[(i-1)%h]; curr = hull[i]; nxt = hull[(i+1)%h]
        ux, uy = prev[0]-curr[0], prev[1]-curr[1]
        vx, vy = nxt[0]-curr[0], nxt[1]-curr[1]
        lenU = math.hypot(ux, uy); lenV = math.hypot(vx, vy)
        if lenU == 0 or lenV == 0:
            keep.append(curr); continue
        dot = ux*vx + uy*vy
        cosA = -dot / (lenU*lenV)
        if cosA <= cosT:  # angle >= theta
            keep.append(curr)
    return keep

if __name__ == "__main__":
    main()
