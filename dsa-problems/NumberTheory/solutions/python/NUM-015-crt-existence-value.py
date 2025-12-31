import sys

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def crt_solve(a, m):
    cur_a = 0
    cur_m = 1
    
    for i in range(len(a)):
        A = a[i]
        M = m[i]
        
        # k * cur_m = A - cur_a (mod M)
        rhs = (A - cur_a) % M
        
        g, x, y = extended_gcd(cur_m, M)
        
        if rhs % g != 0:
            return None
            
        inv = x % (M // g)
        k = (rhs // g) * inv % (M // g)
        
        # New state
        # cur_a = cur_a + k * cur_m
        # cur_m = lcm(cur_m, M)
        
        new_m = cur_m * (M // g)
        cur_a = (cur_a + k * cur_m) % new_m
        cur_m = new_m
        
    return cur_a

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    iterator = iter(data)
    try:
        k = int(next(iterator))
        a = []
        m = []
        for _ in range(k):
            a.append(int(next(iterator)))
            m.append(int(next(iterator)))
            
        res = crt_solve(a, m)
        print("NO" if res is None else res)
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
