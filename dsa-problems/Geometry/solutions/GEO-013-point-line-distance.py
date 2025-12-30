import math

def distance_point_segment(x1: int, y1: int, x2: int, y2: int, px: int, py: int) -> float:
    ux, uy = x2 - x1, y2 - y1
    vx, vy = px - x1, py - y1
    denom = ux*ux + uy*uy
    if denom == 0:
        return math.hypot(vx, vy)
    t = (ux*vx + uy*vy) / denom
    t = max(0.0, min(1.0, t))
    cx = x1 + t * ux
    cy = y1 + t * uy
    return math.hypot(px - cx, py - cy)


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
