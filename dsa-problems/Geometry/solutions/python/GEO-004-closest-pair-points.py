from typing import List, Tuple

def closest_pair(xs: List[int], ys: List[int]) -> int:
    pts = sorted(zip(xs, ys))

    def dist2(a: Tuple[int,int], b: Tuple[int,int]) -> int:
        dx = a[0]-b[0]; dy = a[1]-b[1]
        return dx*dx + dy*dy

    def solve(arr: List[Tuple[int,int]]) -> int:
        n = len(arr)
        if n <= 3:
            best = min(dist2(arr[i], arr[j]) for i in range(n) for j in range(i+1, n))
            arr.sort(key=lambda p: p[1])
            return best
        mid = n//2
        midx = arr[mid][0]
        left = arr[:mid]
        right = arr[mid:]
        d = min(solve(left), solve(right))
        merged = []
        i=j=0
        while i < len(left) and j < len(right):
            if left[i][1] <= right[j][1]:
                merged.append(left[i]); i+=1
            else:
                merged.append(right[j]); j+=1
        merged.extend(left[i:]); merged.extend(right[j:])
        arr[:] = merged
        strip = [p for p in arr if (p[0]-midx)**2 < d]
        for i in range(len(strip)):
            for j in range(i+1, min(i+8, len(strip))):
                dy = strip[j][1] - strip[i][1]
                if dy*dy >= d: break
                d = min(d, dist2(strip[i], strip[j]))
        return d

    if len(pts) != len(set(pts)):
        return 0
    return solve(pts)

def main() -> None:
    import sys
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
        print(closest_pair(xs, ys))
    except StopIteration:
        return

if __name__ == "__main__":
    main()
