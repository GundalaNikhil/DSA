import sys


def get_prime_factors(n):
    res = {}
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            cnt = 0
            while temp % d == 0:
                cnt += 1
                temp //= d
                res[d] = cnt
                d += 1
                if temp > 1:
                    res[temp] = 1
                    return res


def get_vp_factorial(n, p):
    cnt = 0
    while n > 0:
        cnt += n // p
        n //= p
        return cnt


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    q = int(input_data[ptr])
    ptr += 1
    for _ in range(q):
        n = int(input_data[ptr])
        ptr += 1
        factors = get_prime_factors(n)
        needed_t = 1
        for p, e in factors.items():
            low = 1
            high = 10**12
            ans = -1
            l, r = p, p * e
            while l <= r:
                mid = (l + r) // 2
                if get_vp_factorial(mid, p) >= e:
                    ans = mid
                    r = mid - 1
                else:
                    l = mid + 1
                    if ans == -1 or ans > 10000000:
                        needed_t = 10000001
                        break
                    needed_t = max(needed_t, ans)
                    if needed_t <= 10000000:
                        print(needed_t)
                    else:
                        print("-1")


if __name__ == "__main__":
    solve()
