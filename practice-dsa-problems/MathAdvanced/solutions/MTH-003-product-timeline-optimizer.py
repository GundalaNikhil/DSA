import sys


def get_prime_powers(n):
    res = []
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            p_pow = 1
            while temp % d == 0:
                p_pow *= d
                temp //= d
                res.append(p_pow)
                d += 1
                if temp > 1:
                    res.append(temp)
                    return res


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    q = int(input_data[ptr])
    ptr += 1
    out = []
    for _ in range(q):
        n = int(input_data[ptr])
        ptr += 1
        if n == 1:
            out.append("1")
            continue
        powers = get_prime_powers(n)
        max_p_pow = 0
        for p_pow in powers:
            max_p_pow = max(max_p_pow, p_pow)
            if max_p_pow <= 10000000:
                out.append(str(max_p_pow))
            else:
                out.append("-1")
                sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    solve()
