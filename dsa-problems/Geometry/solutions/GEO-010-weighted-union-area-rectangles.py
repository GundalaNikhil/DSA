from typing import List, Tuple

def weighted_area(x1: List[int], y1: List[int], x2: List[int], y2: List[int], w: List[int], W: int) -> int:
    n = len(x1)
    ys = sorted(set(y1 + y2))
    idx = {v:i for i,v in enumerate(ys)}
    events = []
    for i in range(n):
        events.append((x1[i], 1, idx[y1[i]], idx[y2[i]], w[i]))
        events.append((x2[i], -1, idx[y1[i]], idx[y2[i]], w[i]))
    events.sort()

    segN = len(ys) - 1
    add = [0]*(4*segN)
    lenCovered = [0]*(4*segN)

    def pull(node, l, r):
        if add[node] >= W:
            lenCovered[node] = ys[r] - ys[l]
        elif r - l == 1:
            lenCovered[node] = 0
        else:
            lenCovered[node] = lenCovered[node*2] + lenCovered[node*2+1]

    def update(node, l, r, ql, qr, val):
        if qr <= l or r <= ql: return
        if ql <= l and r <= qr:
            add[node] += val
            pull(node, l, r)
            return
        mid = (l + r)//2
        update(node*2, l, mid, ql, qr, val)
        update(node*2+1, mid, r, ql, qr, val)
        pull(node, l, r)

    prevX = events[0][0]
    area = 0
    for i, (x, typ, l, r, wt) in enumerate(events):
        dx = x - prevX
        area += lenCovered[1] * dx
        update(1, 0, segN, l, r, wt if typ==1 else -wt)
        prevX = x
    return area


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
