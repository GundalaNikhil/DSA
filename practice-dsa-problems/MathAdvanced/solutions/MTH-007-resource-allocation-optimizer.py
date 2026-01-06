import sys


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    d, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return d, x, y


def solve_congruence(A, B, M):
    g, x0, y0 = extended_gcd(A, M)
    if B % g != 0:
        return -1
    new_m = M // g
    x = (x0 * (B // g)) % new_m
    if x < 0:
        x += new_m
        return x


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    q_count = int(input_data[ptr])
    ptr += 1
    for _ in range(q_count):
        a = int(input_data[ptr])
        ptr += 1
        d = int(input_data[ptr])
        ptr += 1
        n = int(input_data[ptr])
        ptr += 1
        m = int(input_data[ptr])
        ptr += 1
        if n == 0:
            print(0)
            continue
        s0 = (n % (2 * m)) * (a % m) % (2 * m)
        term2 = (d % (2 * m)) * (n % (2 * m)) % (2 * m) * ((n - 1) % (2 * m)) % (2 * m)
        s0 = (s0 + term2 // 2) % m
        ans = solve_congruence(n % m, (m - s0) % m, m)
        print(ans)


if __name__ == "__main__":
    solve()
