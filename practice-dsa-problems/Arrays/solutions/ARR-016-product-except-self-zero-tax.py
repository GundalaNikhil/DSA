import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        t_tax = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))
    except StopIteration:
        return
    
    MOD = 1_000_000_007
    b = []
    for x in a:
        if x == 0:
            b.append(t_tax)
        else:
            b.append(x)
            
    # Prefix products
    prefix = [1] * (n + 1)
    for i in range(n):
        prefix[i + 1] = (prefix[i] * b[i]) % MOD
        
    # Suffix products
    suffix = [1] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix[i] = (suffix[i + 1] * b[i]) % MOD
        
    res = []
    for i in range(n):
        prod = (prefix[i] * suffix[i + 1]) % MOD
        res.append(prod)
        
    print(*(res))

if __name__ == "__main__":
    solve()
