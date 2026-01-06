import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    p = int(input_data[ptr])
    ptr += 1
    q = int(input_data[ptr])
    ptr += 1
    limit = 10000000
    fact = [1] * (limit + 1)
    for i in range(2, limit + 1):
        fact[i] = (fact[i - 1] * i) % p


def power(a, b, m):
    res = 1
    a %= m
    while b > 0:
        if b & 1:
            res = (res * a) % m
            a = (a * a) % m
            b >>= 1
            return res


def inverse(n, m):
    return power(n, m - 2, m)


out = []
for _ in range(q):
    n = int(input_data[ptr])
    ptr += 1
    k = int(input_data[ptr])
    ptr += 1
    if k == 0:
        out.append(str(fact[n]))
    elif k == n:
        out.append("1")
    elif k > n:
        out.append("0")
    else:
        res = (fact[n] * inverse(fact[k], p)) % p
        out.append(str(res))
        sys.stdout.write("\n".join(out) + "\n")
if __name__ == "__main__":
    solve()
