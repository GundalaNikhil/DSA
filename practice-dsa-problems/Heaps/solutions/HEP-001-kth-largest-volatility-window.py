import sys
from bisect import bisect_left


class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def update(self, i, delta):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
            return s

    def find_kth_desc(self, k, total):
        target = total - k + 1
        idx = 0
        current_sum = 0
        for j in range(18, -1, -1):
            next_idx = idx + (1 << j)
            if next_idx < len(self.tree) and current_sum + self.tree[next_idx] < target:
                idx = next_idx
                current_sum += self.tree[idx]
                return idx + 1


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    k = int(input_data[ptr])
    ptr += 1
    w = int(input_data[ptr])
    ptr += 1
    t_vol = int(input_data[ptr])
    ptr += 1
    a = []
    for _ in range(n):
        a.append(int(input_data[ptr]))
        ptr += 1
        sorted_a = sorted(list(set(a)))
        val_map = {v: i + 1 for i, v in enumerate(sorted_a)}
        rank_to_val = {i + 1: v for i, v in enumerate(sorted_a)}
        res = []
        ft = FenwickTree(len(sorted_a))
        L = 0
        last_bad = -1
        for i in range(n):
            if i > 0:
                if abs(a[i] - a[i - 1]) > t_vol:
                    last_bad = i - 1
                    L_new = max(0, i - w + 1, last_bad + 1)
                    ft.update(val_map[a[i]], 1)
                    while L < L_new:
                        ft.update(val_map[a[L]], -1)
                        L += 1
                        window_size = i - L + 1
                        if window_size >= k:
                            idx = ft.find_kth_desc(k, window_size)
                            res.append(str(rank_to_val[idx]))
                        else:
                            res.append("-1")
                            print(*(res))


if __name__ == "__main__":
    solve()
