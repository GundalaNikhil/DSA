import math

def distance_point_segment(x1: int, y1: int, x2: int, y2: int, px: int, py: int) -> float:
    ux, uy = x2 - x1, y2 - y1
    denom = ux*ux + uy*uy
    if denom == 0:
        return math.hypot(px - x1, py - y1)
    
    vx, vy = px - x1, py - y1
    t = (vx * ux + vy * uy) / denom
    
    if t <= 0:
        return math.hypot(px - x1, py - y1)
    elif t >= 1:
        return math.hypot(px - x2, py - y2)
    else:
        # Distance to line
        # Area formula: abs(cross) / length
        # cross = (B-A) x (P-A)
        cross = ux * vy - uy * vx
        return abs(cross) / math.sqrt(denom)

def main() -> None:
    import sys
    data = list(map(int, sys.stdin.read().strip().split()))
    if len(data) < 6:
        return
    x1, y1, x2, y2, px, py = data[:6]
    val = distance_point_segment(x1, y1, x2, y2, px, py)
    print(f"{val:.6f}")

if __name__ == "__main__":
    main()
