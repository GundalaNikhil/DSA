def longest_repeated(s: str) -> str:
    n = len(s)
    if n == 0:
        return "NONE"
        
    # 1. Build Suffix Array
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
        
    # 2. Build LCP Array
    lcp = [0] * (n - 1)
    k = 0
    for i in range(n):
        if rank[i] == n - 1:
            k = 0
            continue
        j = sa[rank[i] + 1]
        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k += 1
        lcp[rank[i]] = k
        if k > 0:
            k -= 1
            
    # 3. Find Max LCP
    max_len = 0
    start_idx = -1
    
    for i in range(n - 1):
        if lcp[i] > max_len:
            max_len = lcp[i]
            start_idx = sa[i]
            
    if max_len == 0:
        return "NONE"
    return s[start_idx : start_idx + max_len]

def main():
    import sys
sys.setrecursionlimit(200000)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    print(longest_repeated(s))

if __name__ == "__main__":
    main()