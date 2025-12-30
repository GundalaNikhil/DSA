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
    idx = min(range(len(pts)), key=lambda i: (pts[i][0], pts[i][1]))
    return pts[idx:] + pts[:idx]


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
