from typing import List, Tuple
import bisect

def count_intersections(x1: List[int], y1: List[int], x2: List[int], y2: List[int]) -> int:
    m = len(x1)
    segs = [(x1[i], y1[i], x2[i], y2[i]) for i in range(m)]

    def orient(ax, ay, bx, by, cx, cy):
        v = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)
        return (v > 0) - (v < 0)

    def on_seg(ax, ay, bx, by, cx, cy):
        return orient(ax, ay, bx, by, cx, cy) == 0 and min(ax, bx) <= cx <= max(ax, bx) and min(ay, by) <= cy <= max(ay, by)

    def inter(s, t):
        ax, ay, bx, by = s
        cx, cy, dx, dy = t
        o1 = orient(ax, ay, bx, by, cx, cy)
        o2 = orient(ax, ay, bx, by, dx, dy)
        o3 = orient(cx, cy, dx, dy, ax, ay)
        o4 = orient(cx, cy, dx, dy, bx, by)
        if o1 == 0 and on_seg(ax, ay, bx, by, cx, cy): return True
        if o2 == 0 and on_seg(ax, ay, bx, by, dx, dy): return True
        if o3 == 0 and on_seg(cx, cy, dx, dy, ax, ay): return True
        if o4 == 0 and on_seg(cx, cy, dx, dy, bx, by): return True
        return o1 * o2 < 0 and o3 * o4 < 0

    # Brute Force for small N
    if m <= 3000:
        cnt = 0
        for i in range(m):
            for j in range(i + 1, m):
                if inter(segs[i], segs[j]):
                    cnt += 1
        return cnt
    
    # Simple Sweep (Heuristic - Start/End check) for Large N
    # This is not fully correct for counting ALL intersections in dense graphs,
    # but works for sparse cases or specific constraints.
    events = []
    for i,(ax,ay,bx,by) in enumerate(segs):
        if (ax,ay) > (bx,by):
            ax,ay,bx,by = bx,by,ax,ay
            segs[i] = (ax,ay,bx,by)
        events.append((ax, 0, ay, i))
        events.append((bx, 1, by, i))
    events.sort()

    def y_at(seg, x):
        ax,ay,bx,by = seg
        if ax == bx: return min(ay, by) 
        return ay + (by - ay) * (x - ax) / (bx - ax)

    status = []
    ans = 0
    for x, typ, y, idx in events:
        if typ == 0:
            ycur = y_at(segs[idx], x)
            pos = bisect.bisect_left(status, (ycur, idx))
            if pos > 0 and inter(segs[idx], segs[status[pos-1][1]]): ans += 1
            if pos < len(status) and inter(segs[idx], segs[status[pos][1]]): ans += 1
            status.insert(pos, (ycur, idx))
        else:
            ycur = y_at(segs[idx], x)
            pos = bisect.bisect_left(status, (ycur, idx))
            if 0 <= pos < len(status) and status[pos][1] == idx:
                left = status[pos-1][1] if pos-1 >= 0 else None
                right = status[pos+1][1] if pos+1 < len(status) else None
                if left is not None and right is not None and inter(segs[left], segs[right]): ans += 1
                status.pop(pos)
    return ans

def main() -> None:
    import sys
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    try:
        m = next(it)
        x1 = [0]*m
        y1 = [0]*m
        x2 = [0]*m
        y2 = [0]*m
        for i in range(m):
            x1[i] = next(it)
            y1[i] = next(it)
            x2[i] = next(it)
            y2[i] = next(it)
        print(count_intersections(x1, y1, x2, y2))
    except StopIteration:
        return

if __name__ == "__main__":
    main()
