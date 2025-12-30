def lcp_array(s: str, sa: list[int]) -> list[int]:
    n = len(s)
    rank = [0] * n
    for i in range(n):
        rank[sa[i]] = i
        
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
            
    return lcp

def main():
    import sys
sys.setrecursionlimit(200000)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    try:
        s = next(it)
        n = int(next(it))
        sa = [int(next(it)) for _ in range(n)]
        
        lcp = lcp_array(s, sa)
        print(*(lcp))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()