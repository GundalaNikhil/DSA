import sys
import math


def get_convex_hull(points):
    n = len(points)
    if n <= 2:
        return points
    points.sort()


def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


lower = []
for p in points:
    while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) < 0:
        lower.pop()
        lower.append(p)
        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) < 0:
                upper.pop()
                upper.append(p)
                return lower[:-1] + upper[:-1]


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    pts = []
    for i in range(1, n + 1):
        x = int(input_data[ptr])
        ptr += 1
        y = int(input_data[ptr])
        ptr += 1
        pts.append((x, y, i))
        hull_pts = get_convex_hull([(p[0], p[1]) for p in pts])
        print(len(hull_pts))
        for p in hull_pts:
            print(f"{p[0]} {p[1]}")
            if n == 0:
                print(0)
                return
            sum_x = sum(p[0] for p in pts)
            sum_y = sum(p[1] for p in pts)
            cx = sum_x / n
            cy = sum_y / n
            dists = []
            for p in pts:
                d = math.sqrt((p[0] - cx) ** 2 + (p[1] - cy) ** 2)
                dists.append(d)
                mu = sum(dists) / n
                var = sum((d - mu) ** 2 for d in dists) / n
                sigma = math.sqrt(var)
                outliers = []
                for i in range(n):
                    if dists[i] > mu + 2 * sigma:
                        outliers.append(pts[i])
                        print(len(outliers))
                        for p in outliers:
                            print(f"{p[2]} {p[0]} {p[1]}")


if __name__ == "__main__":
    solve()
