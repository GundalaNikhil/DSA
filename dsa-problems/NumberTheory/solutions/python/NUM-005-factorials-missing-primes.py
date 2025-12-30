def factorial_missing_prime(n: int, p: int) -> int:
    if n >= p:
        # Periodic part: (1*2*...*(p-1))^ (n // p) mod p
        # Wilson's Theorem: (p-1)! mod p = p-1 = -1
        # So we need (-1)^(n // p) mod p
        res = pow(p - 1, n // p, p)
        # Remainder part: 1 * 2 * ... * (n % p) mod p
        for i in range(1, (n % p) + 1):
            res = (res * i) % p
        # Recursive call for multiples of p: p, 2p, 3p, ..., (n//p)p
        # These are p * (1, 2, ..., n//p). 
        # Actually the problem says "NOT divisible by p".
        # If numbers are {1, 2, ..., n}, we skip p, 2p, ...
        # The numbers NOT divisible by p are [1..n] \ {p, 2p, ..., (n//p)p}
        # My logic for periodic part already handles this.
        return res
    else:
        res = 1
        for i in range(1, n + 1):
            res = (res * i) % p
        return res

def main():
    import sys
    input_data = sys.stdin.read().strip().split()
    if not input_data: return
    n = int(input_data[0])
    p = int(input_data[1])
    print(factorial_missing_prime(n, p))

if __name__ == "__main__":
    main()
