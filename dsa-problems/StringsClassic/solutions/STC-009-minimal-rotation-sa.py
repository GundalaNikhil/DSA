def minimal_rotation_index(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0
    text = s + s
    m = len(text)
    
    # Build SA
    sa = list(range(m))
    rank = [ord(c) for c in text]
    new_rank = [0] * m
    
    k = 1
    while k < m:
        key_func = lambda i: (rank[i], rank[i + k] if i + k < m else -1)
        sa.sort(key=key_func)
        
        new_rank[sa[0]] = 0
        for i in range(1, m):
            prev = sa[i-1]
            curr = sa[i]
            if key_func(prev) == key_func(curr):
                new_rank[curr] = new_rank[prev]
            else:
                new_rank[curr] = new_rank[prev] + 1
        
        rank = list(new_rank)
        if rank[sa[m-1]] == m - 1:
            break
        k *= 2
        
    for idx in sa:
        if idx < n:
            return idx
    return 0

def main():
    import sys
sys.setrecursionlimit(200000)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    print(minimal_rotation_index(s))

if __name__ == "__main__":
    main()