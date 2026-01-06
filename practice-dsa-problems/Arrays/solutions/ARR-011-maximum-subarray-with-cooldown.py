import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        x_cool = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))
    except StopIteration:
        return

    if n == 0:
        return

    
    f = [-float("inf")] * (n + 1)
    g = [-float("inf")] * (n + 1)
    
    
    for i in range(1, n + 1):
        val = a[i - 1]
        
        # Calculate prev_f based on cooldown
        r = i - x_cool - 2
        prev_f = 0
        if r >= 0: # valid index in f (f is size n+1, r+1 is index)
             # r+1 range: 0 to n.
             prev_f = max(0, f[r + 1])
        else:
             pass
             
        term_prev = g[i - 1] if i > 1 else -float("inf")
        
        g[i] = val + max(term_prev, prev_f)
        
        term_f_prev = f[i-1] if i > 1 else -float("inf")
        f[i] = max(term_f_prev, g[i])
        
    print(f[n])

if __name__ == "__main__":
    solve()
