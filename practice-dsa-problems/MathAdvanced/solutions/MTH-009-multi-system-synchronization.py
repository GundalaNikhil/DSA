import sys


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    d, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return d, x, y


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    q_count = int(input_data[ptr])
    ptr += 1
    for _ in range(q_count):
        k = int(input_data[ptr])
        ptr += 1
        r1, m1 = int(input_data[ptr]), int(input_data[ptr])
        ptr += 2
        possible = True
        for _ in range(k - 1):
            r2, m2 = int(input_data[ptr]), int(input_data[ptr])
            ptr += 2
            if not possible:
                continue
            g, x, y = extended_gcd(m1, m2)
            if (r2 - r1) % g != 0:
                possible = False
                continue
            new_m = (m1 * m2) // g
            r1 = (r1 + m1 * ((r2 - r1) // g * x % (m2 // g))) % new_m
            m1 = new_m
            if possible:
                print(r1 % m1)
            else:
                print("-1")


if __name__ == "__main__":
    solve()
