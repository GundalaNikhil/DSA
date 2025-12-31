def count_exclusive_substrings(a: str, b: str) -> int:
    s = a + "#" + b
    n = len(s)
    split_idx = len(a)
    
    # 1. Build SA
    sa = list(range(n))
    rank = [ord(c) for c in s]
    new_rank = [0] * n
    
    k = 1
    while k < n:
        key_func = lambda i: (rank[i], rank[i + k] if i + k < n else -1)
        sa.sort(key=key_func)
        
        new_rank[sa[0]] = 0
        for i in range(1, n):
            prev = sa[i-1]
            curr = sa[i]
            if key_func(prev) == key_func(curr):
                new_rank[curr] = new_rank[prev]
            else:
                new_rank[curr] = new_rank[prev] + 1
        
        rank = list(new_rank)
        if rank[sa[n-1]] == n - 1:
            break
        k *= 2
        
    # 2. Build LCP (lcp[i] between sa[i-1] and sa[i])
    lcp = [0] * n
    k_val = 0
    for i in range(n):
        if rank[i] == 0:
            k_val = 0
            continue
        j = sa[rank[i] - 1]
        while i + k_val < n and j + k_val < n and s[i + k_val] == s[j + k_val]:
            k_val += 1
        lcp[rank[i]] = k_val
        if k_val > 0:
            k_val -= 1
            
    # 3. Max Match B
    max_match_b = [0] * n
    
    # Forward
    curr_lcp = 0
    for i in range(n):
        if i > 0:
            curr_lcp = min(curr_lcp, lcp[i])
        if sa[i] > split_idx: # From B
            curr_lcp = n
        elif sa[i] < split_idx: # From A
            max_match_b[i] = max(max_match_b[i], curr_lcp)
            
    # Backward
    curr_lcp = 0
    for i in range(n - 1, -1, -1):
        if i < n - 1:
            curr_lcp = min(curr_lcp, lcp[i + 1])
        if sa[i] > split_idx: # From B
            curr_lcp = n
        elif sa[i] < split_idx: # From A
            max_match_b[i] = max(max_match_b[i], curr_lcp)
            
    # 4. Count
    count = 0
    prev_a_lcp = 0
    
    for i in range(n):
        if i > 0:
            prev_a_lcp = min(prev_a_lcp, lcp[i])
            
        if sa[i] < split_idx: # From A
            length = split_idx - sa[i]
            deduct = max(prev_a_lcp, max_match_b[i])
            if length > deduct:
                count += (length - deduct)
            prev_a_lcp = n # Reset for next A
            
    return count

def main():
    import sys
    sys.setrecursionlimit(200000)
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
    a, b = input_data[0], input_data[1]
    print(count_exclusive_substrings(a, b))

if __name__ == "__main__":
    main()