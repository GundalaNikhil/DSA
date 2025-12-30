def threshold_jump(prices: list[int], t: int) -> list[int]:
    n = len(prices)
    # Coordinate Compression
    distinct = sorted(list(set(prices)))
    rank_map = {val: i for i, val in enumerate(distinct)}
    m = len(distinct)
    
    # Segment Tree (Min)
    tree = [float('inf')] * (4 * m)
    
    def update(node, start, end, idx, val):
        if start == end:
            tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            update(2 * node, start, mid, idx, val)
        else:
            update(2 * node + 1, mid + 1, end, idx, val)
        tree[node] = min(tree[2 * node], tree[2 * node + 1])
        
    def query(node, start, end, l, r):
        if r < start or end < l:
            return float('inf')
        if l <= start and end <= r:
            return tree[node]
        mid = (start + end) // 2
        return min(query(2 * node, start, mid, l, r),
                   query(2 * node + 1, mid + 1, end, l, r))
                   
    import bisect
    result = [0] * n
    
    for i in range(n - 1, -1, -1):
        target = prices[i] + t
        # Find rank >= target
        r = bisect.bisect_left(distinct, target)
        
        if r < m:
            nearest_idx = query(1, 0, m - 1, r, m - 1)
            if nearest_idx != float('inf'):
                result[i] = nearest_idx - i
        
        update(1, 0, m - 1, rank_map[prices[i]], i)
        
    return result


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
