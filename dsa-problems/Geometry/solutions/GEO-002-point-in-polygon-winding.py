from typing import List

def classify_point(xs: List[int], ys: List[int], qx: int, qy: int) -> str:
    n = len(xs)
    wn = 0
    for i in range(n):
        j = (i + 1) % n
        xi, yi, xj, yj = xs[i], ys[i], xs[j], ys[j]
        cross = (xj - xi) * (qy - yi) - (yj - yi) * (qx - xi)
        # boundary check
        if cross == 0 and min(xi, xj) <= qx <= max(xi, xj) and min(yi, yj) <= qy <= max(yi, yj):
            return "boundary"
        if yi <= qy < yj and cross > 0:
            wn += 1
        elif yi > qy >= yj and cross < 0:
            wn -= 1
    return "inside" if wn != 0 else "outside"


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
