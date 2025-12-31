from typing import List

def max_overlap(x1: List[int], y1: List[int], x2: List[int], y2: List[int]) -> int:
    n = len(x1)
    ys = sorted(set(y1 + y2))
    idx = {v:i for i,v in enumerate(ys)}
    events = []
    for i in range(n):
        # type -1 for Add, 1 for Remove.
        # Add processed BEFORE Remove => Inclusive X.
        # Y range inclusive [idx[y1], idx[y2]].
        # Segment tree expects [ql, qr). So we pass idx[y2] + 1.
        events.append((x1[i], -1, idx[y1[i]], idx[y2[i]] + 1))
        events.append((x2[i], 1, idx[y1[i]], idx[y2[i]] + 1))
    events.sort()

    m = len(ys) # Points, not intervals
    if m == 0:
        return 0
    
    # Tree size approx 4*m
    add = [0]*(4*m)
    mx = [0]*(4*m)

    def update(node, l, r, ql, qr, val):
        if qr <= l or r <= ql: return
        if ql <= l and r <= qr:
            # Note: val is -1 for Add (type sort order) but we want to Add +1 to weight?
            # No, type -1 is just for sorting.
            # We need to decide what 'val' to add.
            # If type is -1 (Add), we should Add +1.
            # If type is 1 (Remove), we should Add -1.
            # So added value is -Val.
            real_val = -val
            add[node] += real_val
            mx[node] += real_val
            return
        mid = (l + r)//2
        update(node*2, l, mid, ql, qr, val)
        update(node*2+1, mid, r, ql, qr, val)
        mx[node] = add[node] + max(mx[node*2], mx[node*2+1])

    ans = 0
    for x, type_code, l, r in events:
        update(1, 0, m, l, r, type_code)
        ans = max(ans, mx[1])
    return ans

def main() -> None:
    import sys
    # Use generator input reading for robustness
    sys.setrecursionlimit(200000)
    def input_gen():
        for line in sys.stdin:
            for token in line.split():
                yield token
    it = input_gen()
    try:
        m = int(next(it))
        x1=[]; y1=[]; x2=[]; y2=[]
        for _ in range(m):
            x1.append(int(next(it))); y1.append(int(next(it))); x2.append(int(next(it))); y2.append(int(next(it)))
        print(max_overlap(x1, y1, x2, y2))
    except StopIteration:
        return

if __name__ == "__main__":
    main()
