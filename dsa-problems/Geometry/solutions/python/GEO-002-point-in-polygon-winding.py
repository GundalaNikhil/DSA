from typing import List

def classify_point(xs: List[int], ys: List[int], qx: int, qy: int) -> str:
    n = len(xs)
    wn = 0
    for i in range(n):
        xi, yi = xs[i], ys[i]
        xj, yj = xs[(i + 1) % n], ys[(i + 1) % n]
        
        # Check boundary using cross product and dot product
        # Point Q on segment P_i P_j if Cross(P_i-Q, P_j-Q) == 0 and Dot(P_i-Q, P_j-Q) <= 0
        cross = (xi - qx) * (yj - qy) - (xj - qx) * (yi - qy)
        if cross == 0:
            dot = (xi - qx) * (xj - qx) + (yi - qy) * (yj - qy)
            if dot <= 0:
                return "boundary"
        
        # Winding number
        # Upward crossing
        if yi <= qy:
            if yj > qy:
                # Q to left of edge
                if (xj - xi) * (qy - yi) - (yj - yi) * (qx - xi) > 0:
                    wn += 1
        else:
            # Downward crossing
            if yj <= qy:
                 # Q to right of edge
                 if (xj - xi) * (qy - yi) - (yj - yi) * (qx - xi) < 0:
                     wn -= 1
                     
    return "inside" if wn != 0 else "outside"

def main() -> None:
    import sys
    # Read all tokens at once to handle newlines/spaces robustly
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
        qx = next(it)
        qy = next(it)
        print(classify_point(xs, ys, qx, qy))
    except StopIteration:
        return

if __name__ == "__main__":
    main()
