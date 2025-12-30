from typing import List

def max_overlap(x1: List[int], y1: List[int], x2: List[int], y2: List[int]) -> int:
    n = len(x1)
    ys = sorted(set(y1 + y2))
    idx = {v:i for i,v in enumerate(ys)}
    events = []
    for i in range(n):
        events.append((x1[i], 1, idx[y1[i]], idx[y2[i]]))
        events.append((x2[i], -1, idx[y1[i]], idx[y2[i]]))
    events.sort()

    m = len(ys) - 1
    add = [0]*(4*m)
    mx = [0]*(4*m)

    def pull(node):
        mx[node] = add[node] + max(mx[node*2], mx[node*2+1])

    def update(node, l, r, ql, qr, val):
        if qr <= l or r <= ql: return
        if ql <= l and r <= qr:
            add[node] += val
            mx[node] += val
            return
        mid = (l + r)//2
        update(node*2, l, mid, ql, qr, val)
        update(node*2+1, mid, r, ql, qr, val)
        mx[node] = add[node] + max(mx[node*2], mx[node*2+1])

    ans = 0
    for x, typ, l, r in events:
        update(1, 0, m, l, r, typ)
        ans = max(ans, mx[1])
    return ans


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
