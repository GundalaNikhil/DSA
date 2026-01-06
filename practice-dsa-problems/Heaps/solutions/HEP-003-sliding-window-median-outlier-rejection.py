import sys
import heapq


class MedianFinder:
    def __init__(self):
        self.smaller = []
        self.larger = []
        self.deleted = {}

    def _clean_heaps(self):
        while self.smaller and self.deleted.get(-self.smaller[0], 0) > 0:
            val = -heapq.heappop(self.smaller)
            self.deleted[val] -= 1
            while self.larger and self.deleted.get(self.larger[0], 0) > 0:
                val = heapq.heappop(self.larger)
                self.deleted[val] -= 1

    def add(self, num):
        if not self.smaller or num <= -self.smaller[0]:
            heapq.heappush(self.smaller, -num)
        else:
            heapq.heappush(self.larger, num)
            self.rebalance()

    def remove(self, num):
        self.deleted[num] = self.deleted.get(num, 0) + 1
        self._clean_heaps()
        self.rebalance()

    def rebalance(self):
        self._clean_heaps()
        pass


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    w = int(input_data[ptr])
    ptr += 1
    a = []
    for _ in range(n):
        a.append(int(input_data[ptr]))
        ptr += 1


def get_window_median(win):
    s = sorted(win)
    return s[(w - 1) // 2]


results = []
for i in range(n - w + 1):
    window = a[i : i + w]
    raw_m = get_window_median(window)
    is_outlier = [x > 2 * raw_m for x in window]
    adj_window = list(window)
    for j in range(w):
        if is_outlier[j]:
            lx = -1
            for k in range(j - 1, -1, -1):
                if not is_outlier[k]:
                    lx = i + k
                    break
                rx = -1
                for k in range(j + 1, w):
                    if not is_outlier[k]:
                        rx = i + k
                        break
                    if lx != -1 and rx != -1:
                        adj_window[j] = (a[lx] + a[rx]) // 2
                    elif lx != -1:
                        adj_window[j] = a[lx]
                    elif rx != -1:
                        adj_window[j] = a[rx]
                        results.append(str(get_window_median(adj_window)))
                        print(*(results))
if __name__ == "__main__":
    solve()
