from collections import deque

def sort_with_swaps(arr: list[int], S: int) -> list[int]:
    n = len(arr)
    q0 = deque([i for i, x in enumerate(arr) if x == 0])
    q1 = deque([i for i, x in enumerate(arr) if x == 1])
    q2 = deque([i for i, x in enumerate(arr) if x == 2])

    bit = [0] * (n + 1)

    def update(i, val):
        while i <= n:
            bit[i] += val
            i += i & (-i)

    def query(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & (-i)
        return s

    for i in range(n):
        update(i + 1, 1)

    res = []
    for _ in range(n):
        idx0 = q0[0] if q0 else None
        idx1 = q1[0] if q1 else None
        idx2 = q2[0] if q2 else None

        cost0 = query(idx0) if idx0 is not None else float('inf')
        cost1 = query(idx1) if idx1 is not None else float('inf')

        if cost0 <= S:
            S -= cost0
            res.append(0)
            q0.popleft()
            update(idx0 + 1, -1)
        elif cost1 <= S:
            S -= cost1
            res.append(1)
            q1.popleft()
            update(idx1 + 1, -1)
        else:
            # Pick min index
            min_idx = float('inf')
            if idx0 is not None: min_idx = min(min_idx, idx0)
            if idx1 is not None: min_idx = min(min_idx, idx1)
            if idx2 is not None: min_idx = min(min_idx, idx2)

            if idx0 is not None and min_idx == idx0:
                res.append(0)
                q0.popleft()
                update(idx0 + 1, -1)
            elif idx1 is not None and min_idx == idx1:
                res.append(1)
                q1.popleft()
                update(idx1 + 1, -1)
            else:
                res.append(2)
                q2.popleft()
                update(idx2 + 1, -1)

    return res

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    s = int(input())
    result = sort_colors_swaps(arr, s)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
