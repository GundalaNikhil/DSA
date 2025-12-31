import sys

def power(base, exp, mod):
    res = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res

def lcm_range(a, l, r, MOD):
    max_exponents = {}
    
    for i in range(l, r + 1):
        num = a[i]
        d = 2
        while d * d <= num:
            if num % d == 0:
                count = 0
                while num % d == 0:
                    num //= d
                    count += 1
                max_exponents[d] = max(max_exponents.get(d, 0), count)
            d += 1
        if num > 1:
            max_exponents[num] = max(max_exponents.get(num, 0), 1)
            
    ans = 1
    for p, e in max_exponents.items():
        ans = (ans * power(p, e, MOD)) % MOD
        
    return ans

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    try:
        n = int(next(iterator))
        q = int(next(iterator))
        MOD = int(next(iterator))
        a = [int(next(iterator)) for _ in range(n)]
        
        results = []
        for _ in range(q):
            l = int(next(iterator))
            r = int(next(iterator))
            results.append(str(lcm_range(a, l, r, MOD)))
            
        print('\n'.join(results))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
