def count_distinct(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0
        
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
        
    # 2. Build LCP Sum
    lcp_sum = 0
    k = 0
    for i in range(n):
        if rank[i] == n - 1:
            k = 0
            continue
        j = sa[rank[i] + 1]
        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k += 1
        lcp_sum += k
        if k > 0:
            k -= 1
            
    total_substrings = n * (n + 1) // 2
    return total_substrings - lcp_sum

def main():
    import sys
sys.setrecursionlimit(200000)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    print(count_distinct(s))

if __name__ == "__main__":
    main()