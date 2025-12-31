import math
from typing import List, Tuple

EPS = 1e-9

def half_plane_intersection(A: List[int], B: List[int], C: List[int]) -> List[Tuple[float, float]]:
    lines = []
    for a, b, c in zip(A, B, C):
        ang = math.atan2(b, a)
        lines.append((ang, a, b, c))
    # sort by angle, tie by offset along the normal (more restrictive first)
    lines.sort(key=lambda t: (t[0], t[3] / math.hypot(t[1], t[2])))

    # prune parallel lines keeping the tightest
    pruned = []
    for L in lines:
        if pruned and abs(L[0] - pruned[-1][0]) < EPS:
            normL = math.hypot(L[1], L[2])
            normP = math.hypot(pruned[-1][1], pruned[-1][2])
            if L[3] / normL < pruned[-1][3] / normP:
                pruned[-1] = L
        else:
            pruned.append(L)
    lines = pruned

    def intersect(L1, L2):
        _, a1, b1, c1 = L1
        _, a2, b2, c2 = L2
        det = a1 * b2 - a2 * b1
        if abs(det) < EPS:
            return None
        x = (c1 * b2 - c2 * b1) / det
        y = (a1 * c2 - a2 * c1) / det
        return (x, y)

    def outside(p, L):
        _, a, b, c = L
        return a * p[0] + b * p[1] - c > EPS

    dq = []
    for L in lines:
        while len(dq) >= 2:
            p = intersect(dq[-2], dq[-1])
            if p is None or not outside(p, L):
                break
            dq.pop()
        while len(dq) >= 2:
            p = intersect(dq[0], dq[1])
            if p is None or not outside(p, L):
                break
            dq.pop(0)
        dq.append(L)

    # final cleanup to close the polygon
    while len(dq) >= 3:
        p = intersect(dq[-2], dq[-1])
        if p is None or not outside(p, dq[0]):
            break
        dq.pop()
    while len(dq) >= 3:
        p = intersect(dq[0], dq[1])
        if p is None or not outside(p, dq[-1]):
            break
        dq.pop(0)

    if len(dq) < 3:
        return []
    pts = []
    for i in range(len(dq)):
        p = intersect(dq[i], dq[(i + 1) % len(dq)])
        if p is None:
            return []
        pts.append(p)
    # rotate to lowest x, then y
    if not pts:
        return []

    # Filter duplicates
    unique_pts = []
    for p in pts:
        if not unique_pts:
            unique_pts.append(p)
        else:
            if math.hypot(p[0]-unique_pts[-1][0], p[1]-unique_pts[-1][1]) > EPS:
                unique_pts.append(p)
    # Check last vs first
    if len(unique_pts) > 1 and math.hypot(unique_pts[0][0]-unique_pts[-1][0], unique_pts[0][1]-unique_pts[-1][1]) < EPS:
        unique_pts.pop()
    
    if len(unique_pts) < 3:
        return []
        
    pts = unique_pts
    idx = min(range(len(pts)), key=lambda i: (pts[i][0], pts[i][1]))
    return pts[idx:] + pts[:idx]

def main() -> None:
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    try:
        m = int(next(it))
        A,B,C = [],[],[]
        for _ in range(m):
            A.append(int(next(it)))
            B.append(int(next(it)))
            C.append(int(next(it)))
        poly = half_plane_intersection(A,B,C)
        if not poly:
            print("EMPTY")
        else:
            print(len(poly))
            for x,y in poly:
                print(f"{x:.6f} {y:.6f}")
    except StopIteration:
        return

if __name__ == "__main__":
    main()
