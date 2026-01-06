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


def legendre_symbol(a, p):
    ls = power(a, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    q_count = int(input_data[ptr])
    ptr += 1
    for _ in range(q_count):
        p = int(input_data[ptr])
        ptr += 1
        e = int(input_data[ptr])
        ptr += 1
        a = int(input_data[ptr])
        ptr += 1
        pe = p**e
        if a == 0:
            print(p ** (e - (e + 1) // 2))
            continue
        v = 0
        temp_a = a
        while temp_a % p == 0:
            v += 1
            temp_a //= p
            if v % 2 != 0:
                print(0)
                continue
            target_mod = e - v
            if legendre_symbol(temp_a % p, p) != 1:
                print(0)
                continue
            print(2 * (p ** (v // 2)))


if __name__ == "__main__":
    solve()
