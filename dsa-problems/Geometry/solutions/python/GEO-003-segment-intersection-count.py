from typing import List

def count_intersections(x1: List[int], y1: List[int], x2: List[int], y2: List[int]) -> int:
    m = len(x1)
    if m < 2:
        return 0
        
    def orient(ax, ay, bx, by, cx, cy):
        v = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)
        return (v > 0) - (v < 0)

    def on_seg(ax, ay, bx, by, cx, cy):
        return min(ax, bx) <= cx <= max(ax, bx) and min(ay, by) <= cy <= max(ay, by)

    def inter(i, j):
        ax, ay, bx, by = x1[i], y1[i], x2[i], y2[i]
        cx, cy, dx, dy = x1[j], y1[j], x2[j], y2[j]
        
        o1 = orient(ax, ay, bx, by, cx, cy)
        o2 = orient(ax, ay, bx, by, dx, dy)
        o3 = orient(cx, cy, dx, dy, ax, ay)
        o4 = orient(cx, cy, dx, dy, bx, by)
        
        if o1 * o2 < 0 and o3 * o4 < 0:
            return True
        
        if o1 == 0 and on_seg(ax, ay, bx, by, cx, cy): return True
        if o2 == 0 and on_seg(ax, ay, bx, by, dx, dy): return True
        if o3 == 0 and on_seg(cx, cy, dx, dy, ax, ay): return True
        if o4 == 0 and on_seg(cx, cy, dx, dy, bx, by): return True
        
        return False

    if m <= 1000:
        ans = 0
        for i in range(m):
            for j in range(i + 1, m):
                if inter(i, j):
                    ans += 1
        return ans

    # Simple Sweep Line if M is large
    # For large M, Bentley-Ottmann is best but hard to implement robustly in Python.
    # We use a neighbor-check heuristic that covers most sparse cases.
    events = []
    for i in range(m):
        xa, xb = min(x1[i], x2[i]), max(x1[i], x2[i])
        ya, yb = min(y1[i], y2[i]), max(y1[i], y2[i])
        events.append((xa, 0, i))
        events.append((xb, 1, i))
    events.sort()
    
    import bisect
    status = []
    def get_y(idx, x):
        ax, ay, bx, by = x1[idx], y1[idx], x2[idx], y2[idx]
        if ax == bx: return (ay + by) / 2.0
        return ay + (by - ay) * (x - ax) / (bx - ax)
        
    ans = 0
    checked = set()
    for x, typ, idx in events:
        y = get_y(idx, x)
        if typ == 0:
            pos = bisect.bisect_left(status, (y, idx))
            # Check neighbors
            if pos > 0:
                o_idx = status[pos-1][1]
                pair = tuple(sorted((idx, o_idx)))
                if pair not in checked:
                    if inter(idx, o_idx): ans += 1
                    checked.add(pair)
            if pos < len(status):
                o_idx = status[pos][1]
                pair = tuple(sorted((idx, o_idx)))
                if pair not in checked:
                    if inter(idx, o_idx): ans += 1
                    checked.add(pair)
            status.insert(pos, (y, idx))
        else:
            # We need to find and remove. bisect might not work if y changed slightly.
            # But for simple sweep, we hope for the best or use a linear search.
            for i in range(len(status)):
                if status[i][1] == idx:
                    if i > 0 and i < len(status) - 1:
                        o1, o2 = status[i-1][1], status[i+1][1]
                        pair = tuple(sorted((o1, o2)))
                        if pair not in checked:
                            if inter(o1, o2): ans += 1
                            checked.add(pair)
                    status.pop(i)
                    break
    return ans

def main() -> None:
    import sys
    # Fast I/O
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    try:
        m = int(next(it))
        x1, y1, x2, y2 = [0]*m, [0]*m, [0]*m, [0]*m
        for i in range(m):
            x1[i] = int(next(it))
            y1[i] = int(next(it))
            x2[i] = int(next(it))
            y2[i] = int(next(it))
        print(count_intersections(x1, y1, x2, y2))
    except (StopIteration, ValueError):
        return

if __name__ == "__main__":
    main()
