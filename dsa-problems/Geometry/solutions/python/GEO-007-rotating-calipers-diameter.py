from typing import List, Tuple

def diameter_squared(xs: List[int], ys: List[int]) -> int:
    n = len(xs)
    pts = [(xs[i], ys[i]) for i in range(n)]

    def cross(a, b, c):
        return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

    def dist2(a, b):
        dx = a[0]-b[0]; dy = a[1]-b[1]
        return dx*dx + dy*dy

    if n == 1:
        return 0
    j = 1
    best = 0
    for i in range(n):
        ni = (i+1)%n
        while cross(pts[i], pts[ni], pts[(j+1)%n]) > cross(pts[i], pts[ni], pts[j]):
            j = (j+1)%n
        best = max(best, dist2(pts[i], pts[j]), dist2(pts[ni], pts[j]))
    return best

if __name__ == "__main__":
    main()
