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


def check_mr(n, witnesses):
    if n < 2:
        return "COMPOSITE", 0
    if n == 2:
        return "PRIME", 0
    if n % 2 == 0:
        return "COMPOSITE", 0
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
        evaluated = 0
        for a in witnesses:
            if a >= n:
                break
            evaluated += 1
            x = power(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(s - 1):
                x = (x * x) % n
                if x == n - 1:
                    break
            else:
                return "COMPOSITE", evaluated
            return "PRIME", evaluated


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    q = int(input_data[ptr])
    ptr += 1
    limit = 10**6
    is_p = [True] * (limit + 1)
    is_p[0] = is_p[1] = False
    small_primes = []
    for i in range(2, limit + 1):
        if is_p[i]:
            small_primes.append(i)
            for j in range(i * i, limit + 1, i):
                is_p[j] = False
                witness_list = [2, 3, 5, 7, 11, 13]
                for _ in range(q):
                    x = int(input_data[ptr])
                    ptr += 1
                    if x < 2:
                        print("COMPOSITE 0")
                        continue
                    is_small_div = False
                    if x <= limit:
                        if is_p[x]:
                            print("PRIME 0")
                        else:
                            print("COMPOSITE 0")
                            continue
                        for p in small_primes:
                            if p * p > x:
                                break
                            if x % p == 0:
                                is_small_div = True
                                break
                            if is_small_div:
                                print("COMPOSITE 0")
                                continue
                            res, k = check_mr(x, witness_list)
                            print(f"{res} {k}")


if __name__ == "__main__":
    solve()
