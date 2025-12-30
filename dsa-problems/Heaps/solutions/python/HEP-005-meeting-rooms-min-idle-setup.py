import sys
from bisect import bisect_right

class Solution:
    def min_total_slack(self, meetings: list, k: int, s: int) -> int:
        meetings.sort(key=lambda x: x[0])
        unused = k

        # Coordinate-compress possible free times (end + s).
        coords = sorted({end + s for _, end in meetings})
        rank = {val: i for i, val in enumerate(coords)}
        n = len(coords)
        tree = [0] * (4 * n)

        def update(node, left, right, idx, delta):
            if left == right:
                tree[node] += delta
                return
            mid = (left + right) // 2
            if idx <= mid:
                update(node * 2, left, mid, idx, delta)
            else:
                update(node * 2 + 1, mid + 1, right, idx, delta)
            tree[node] = tree[node * 2] + tree[node * 2 + 1]

        def query_rightmost(node, left, right, r_limit):
            if left > r_limit or tree[node] == 0:
                return -1
            if left == right:
                return left
            mid = (left + right) // 2
            res = query_rightmost(node * 2 + 1, mid + 1, right, r_limit)
            if res != -1:
                return res
            return query_rightmost(node * 2, left, mid, r_limit)

        total_slack = 0
        for start, end in meetings:
            idx = bisect_right(coords, start) - 1
            best_rank = -1
            if idx >= 0:
                best_rank = query_rightmost(1, 0, n - 1, idx)

            if best_rank != -1:
                free_time = coords[best_rank]
                total_slack += start - free_time
                update(1, 0, n - 1, best_rank, -1)
            else:
                # Use a fresh room; first meeting in a room has 0 slack.
                unused -= 1

            update(1, 0, n - 1, rank[end + s], 1)

        return total_slack

def min_total_slack(meetings: list, k: int, s: int) -> int:
    solver = Solution()
    return solver.min_total_slack(meetings, k, s)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        k = int(next(it))
        s = int(next(it))
        meetings = []
        for _ in range(n):
            start = int(next(it))
            end = int(next(it))
            meetings.append([start, end])
        
        result = min_total_slack(meetings, k, s)
        print(result)
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
