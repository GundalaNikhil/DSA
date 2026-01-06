import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    q = int(input_data[ptr])
    ptr += 1
def get_comb(n, k, m):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1 % m
    if k > n // 2:
        k = n - k
        factors = []
        temp = m
        d = 2
        while d * d <= temp:
            if temp % d == 0:
                pp = 1
                while temp % d == 0:
                    pp *= d
                    temp //= d
                    factors.append((d, pp))
                    d += 1
                    if temp > 1:
                        factors.append((temp, temp))
                        results = []
                        for p, pe in factors:
def get_val(num, p_val):
    res = 1
    cnt = 0
    for i in range(num - k + 1, num + 1):
        x = i
        while x > 0 and x % p_val == 0:
            cnt += 1
            x //= p_val
            res = (res * x) % pe
            denom = 1
            for i in range(1, k + 1):
                x = i
                while x > 0 and x % p_val == 0:
                    cnt -= 1
                    x //= p_val
                    denom = (denom * x) % pe
def inv(a, m_mod):
def egcd(aa, bb):
    if aa == 0:
        return bb, 0, 1
    d_res, x1, y1 = egcd(
    bb % aa, aa
    )
    return (
d_res,
y1 - (bb // aa) * x1,
x1,
)
_, x_res, _ = egcd(a, m_mod)
return x_res % m_mod
final = (res * inv(denom, pe)) % pe
final = (
final * pow(p_val, cnt, pe)
) % pe
results.append((final, pe))
get_val(n, p)
ans_r, ans_m = results[0]
def egcd(aa, bb):
    if aa == 0:
        return bb, 0, 1
    d_res, x1, y1 = egcd(
    bb % aa, aa
    )
    return (
d_res,
y1 - (bb // aa) * x1,
x1,
)
for i in range(1, len(results)):
    r2, m2 = results[i]
    g, x, y = egcd(ans_m, m2)
    new_m = ans_m * m2 // g
    ans_r = (
    ans_r
    + ans_m
    * (
    (r2 - ans_r)
    // g
    * x
    % (m2 // g)
    )
    ) % new_m
    return ans_r % m
for _ in range(q):
    n = int(input_data[ptr])
    ptr += 1
    k = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    print(get_comb(n, k, m))
if __name__ == "__main__":
    solve()