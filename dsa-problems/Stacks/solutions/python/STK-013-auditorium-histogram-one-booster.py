def max_area_with_boost(h: list[int], b: int) -> int:
    n = len(h)
    tree = [0] * (4 * n)
    
    def build(node, start, end):
        if start == end:
            tree[node] = h[start]
        else:
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            tree[node] = min(tree[2 * node], tree[2 * node + 1])
            
    build(1, 0, n - 1)
    
    def find_last_less(node, start, end, l, r, val):
        if l > r or tree[node] >= val:
            return -1
        if start == end:
            return start
        mid = (start + end) // 2
        res = -1
        if mid < r:
            res = find_last_less(2 * node + 1, mid + 1, end, l, r, val)
        if res != -1:
            return res
        if l <= mid:
            return find_last_less(2 * node, start, mid, l, r, val)
        return -1
        
    def find_first_less(node, start, end, l, r, val):
        if l > r or tree[node] >= val:
            return -1
        if start == end:
            return start
        mid = (start + end) // 2
        res = -1
        if l <= mid:
            res = find_first_less(2 * node, start, mid, l, r, val)
        if res != -1:
            return res
        if mid < r:
            return find_first_less(2 * node + 1, mid + 1, end, l, r, val)
        return -1
        
    max_area = 0
    
    for i in range(n):
        # Case 1: Boosted h[i]
        boosted_h = h[i] + b
        L = find_last_less(1, 0, n - 1, 0, i - 1, boosted_h)
        R = find_first_less(1, 0, n - 1, i + 1, n - 1, boosted_h)
        if R == -1: R = n
        max_area = max(max_area, boosted_h * (R - L - 1))
        
        # Case 2: Normal h[i]
        normal_h = h[i]
        L1 = find_last_less(1, 0, n - 1, 0, i - 1, normal_h)
        R1 = find_first_less(1, 0, n - 1, i + 1, n - 1, normal_h)
        if R1 == -1: R1 = n
        
        max_area = max(max_area, normal_h * (R1 - L1 - 1))
        
        if L1 != -1 and h[L1] + b >= normal_h:
            L2 = find_last_less(1, 0, n - 1, 0, L1 - 1, normal_h)
            max_area = max(max_area, normal_h * (R1 - L2 - 1))
            
        if R1 != n and h[R1] + b >= normal_h:
            R2 = find_first_less(1, 0, n - 1, R1 + 1, n - 1, normal_h)
            if R2 == -1: R2 = n
            max_area = max(max_area, normal_h * (R2 - L1 - 1))
            
    return max_area


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
