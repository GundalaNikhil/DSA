import sys
import heapq

# Helper class for updating Fenwick Tree
def update(bit, i, val):
    while i < len(bit):
        bit[i] += val
        i += i & (-i)

def query(bit, i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & (-i)
    return s

def find_kth_rank(count_bit, k):
    # Find smallest index idx such that query(count_bit, idx) >= k
    # We use binary lifting on the BIT structure for O(log N)
    idx = 0
    n = len(count_bit)
    # Start with highest power of 2 less than n
    bit_mask = 1 << (n.bit_length() - 1)
    
    current_idx = 0
    for i in range(n.bit_length() - 1, -1, -1):
        next_idx = current_idx + (1 << i)
        if next_idx < n and count_bit[next_idx] < k:
            current_idx = next_idx
            k -= count_bit[current_idx]
            
    return current_idx + 1

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        w = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))
    except StopIteration:
        return


    sorted_a = sorted(list(set(a)))
    rank_map = {val: i + 1 for i, val in enumerate(sorted_a)}
    m = len(sorted_a)
    
    count_bit = [0] * (m + 1)
    sum_bit = [0] * (m + 1)
    
    ans = []
    
    for i in range(n):
        val = a[i]
        r = rank_map[val]
        
        # Add current
        update(count_bit, r, 1)
        update(sum_bit, r, val)
        
        # Remove old
        if i >= w:
            old_val = a[i - w]
            old_r = rank_map[old_val]
            update(count_bit, old_r, -1)
            update(sum_bit, old_r, -old_val)
            
        if i >= w - 1:
            # Current window size is w
            # Find median. Median is at rank (w + 1) // 2
            mid_k = (w + 1) // 2
            
            median_rank = find_kth_rank(count_bit, mid_k) 
            
            median_val = sorted_a[median_rank - 1]
            
            
            
            cnt_le = query(count_bit, median_rank)
            sum_le = query(sum_bit, median_rank)
            
            cnt_total = w
            sum_total = query(sum_bit, m)
            
            cnt_gt = cnt_total - cnt_le
            sum_gt = sum_total - sum_le
            
            cost = (cnt_le * median_val - sum_le) + (sum_gt - cnt_gt * median_val)
            
            ans.append(str(cost))
            
    print(*(ans))

if __name__ == "__main__":
    solve()
