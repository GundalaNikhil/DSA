def longest_common_substring(a: str, b: str) -> int:
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
        
    # 2. Build LCP
    lcp = [0] * (n - 1)
    k_val = 0
    for i in range(n):
        if rank[i] == n - 1:
            k_val = 0
            continue
        j = sa[rank[i] + 1]
        while i + k_val < n and j + k_val < n and s[i + k_val] == s[j + k_val]:
            k_val += 1
        lcp[rank[i]] = k_val
        if k_val > 0:
            k_val -= 1
            
    # 3. Find Max LCP
    max_len = 0
    for i in range(n - 1):
        idx1 = sa[i]
        idx2 = sa[i+1]
        
        from_a = idx1 < split_idx
        from_b = idx2 < split_idx
        
        if from_a != from_b:
            max_len = max(max_len, lcp[i])
            
    return max_len

def main():
    import sys
    sys.setrecursionlimit(200000)
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
    a, b = input_data[0], input_data[1]
    print(longest_common_substring(a, b))

if __name__ == "__main__":
    main()