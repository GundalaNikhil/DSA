import sys

memo = {}


def get_phi_sum(n):
    if n <= 10**6:
        return pre_phi_sum[n]
    if n in memo:
        return memo[n]
    res = n * (n + 1) // 2
    l = 2
    while l <= n:
        r = n // (n // l)
        res -= (r - l + 1) * get_phi_sum(n // l)
        l = r + 1
        memo[n] = res
        return res
    pre_phi_sum = []


def precompute():
    limit = 10**6
    phi = list(range(limit + 1))
    for i in range(2, limit + 1):
        if phi[i] == i:
            for j in range(i, limit + 1, i):
                phi[j] -= phi[j] // i
                global pre_phi_sum
                pre_phi_sum = [0] * (limit + 1)
                for i in range(1, limit + 1):
                    pre_phi_sum[i] = pre_phi_sum[i - 1] + phi[i]


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    precompute()
    ptr = 0
    q = int(input_data[ptr])
    ptr += 1
    for _ in range(q):
        n = int(input_data[ptr])
        ptr += 1
        print(get_phi_sum(n))


if __name__ == "__main__":
    solve()
