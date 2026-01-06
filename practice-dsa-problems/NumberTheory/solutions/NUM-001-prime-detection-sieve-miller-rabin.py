import sys
def power(a, b, m):
    res = 1
    a %= m
    while b > 0:
        if b & 1:
            res = (res * a) % m
        a = (a * a) % m
        b >>= 1
    return res

def is_prime_mr(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
        
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
        
    witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for a in witnesses:
        if a >= n:
            break
        x = power(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    
    # Check if we have enough input
    if ptr >= len(input_data):
        return
        
    n_limit = int(input_data[ptr])
    ptr += 1
    
    if ptr >= len(input_data):
        return
        
    q_count = int(input_data[ptr])
    ptr += 1
    
    # Sieve of Eratosthenes
    # Ensure n_limit is reasonable for sieve array
    is_prime_sieve = [True] * (n_limit + 1)
    if n_limit >= 2:
        is_prime_sieve[0] = is_prime_sieve[1] = False
    
    primes = []
    for i in range(2, n_limit + 1):
        if is_prime_sieve[i]:
            primes.append(i)
            # Standard Sieve Optimization: start from i*i
            # Nested loop is fine here as it's part of Precomputation
            if i * i <= n_limit:
                for j in range(i * i, n_limit + 1, i):
                    is_prime_sieve[j] = False
                    
    # Query Processing Loop - THIS MUST BE SEPARATE
    for _ in range(q_count):
        if ptr >= len(input_data):
            break
        x = int(input_data[ptr])
        ptr += 1
        
        if x <= n_limit:
            if is_prime_sieve[x]:
                print("PRIME")
            else:
                print("COMPOSITE")
        else:
            # Check divisibility by small primes first
            is_divisible = False
            for p in primes:
                if p * p > x:
                    break
                if x % p == 0:
                    is_divisible = True
                    break
                    
            if is_divisible:
                print("COMPOSITE")
            else:
                # Use Miller-Rabin for large numbers
                if is_prime_mr(x):
                    print("PRIME")
                else:
                    print("COMPOSITE")
if __name__ == '__main__':
    solve()