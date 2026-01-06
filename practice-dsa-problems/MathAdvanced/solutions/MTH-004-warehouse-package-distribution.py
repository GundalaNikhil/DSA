import sys


def floor_sum(n, m, a, b):
    ans = 0
    if a >= m:
        ans += (n - 1) * n * (a // m) // 2
        a %= m
        if b >= m:
            ans += n * (b // m)
            b %= m
            y_max = (a * n + b) // m
            x_max = y_max * m - b
            if y_max == 0:
                return ans
            ans += (n - (x_max + a - 1) // a) * y_max
            ans += floor_sum(y_max, a, m, (a - x_max % a) % a)
            return ans


def floor_sum_atc(n, m, a, b):
    ans = 0
    if a >= m:
        ans += (n - 1) * n * (a // m) // 2
        a %= m
        if b >= m:
            ans += n * (b // m)
            b %= m
            y_max = (a * n + b) // m
            x_max = y_max * m - b
            if y_max == 0:
                return ans
            ans += (n - (x_max + a - 1) // a) * y_max
            ans += floor_sum_atc(y_max, a, m, (a - x_max % a) % a)
            return ans


def floor_sum_impl(n, m, a, b):
    ans = 0
    if a >= m:
        ans += (n - 1) * n * (a // m) // 2
        a %= m
        if b >= m:
            ans += n * (b // m)
            b %= m
            y_max = (a * n + b) // m
            x_max = y_max * m - b
            if y_max == 0:
                return ans
            ans += (n - (x_max + a - 1) // a) * y_max
            ans += floor_sum_impl(y_max, a, m, (a - x_max % a) % a)
            return ans


def atc_floor_sum(n, m, a, b):
    ans = 0
    if a >= m:
        ans += (n - 1) * n * (a // m) // 2
        a %= m
        if b >= m:
            ans += n * (b // m)
            b %= m
            y_max = (a * n + b) // m
            if y_max == 0:
                return ans
            x_max = y_max * m - b
            ans += (n - (x_max + a - 1) // a) * y_max
            ans += atc_floor_sum(y_max, a, m, (a - x_max % a) % a)
            return ans


def floor_sum_simple(n, m, a, b):
    res = 0
    while True:
        if a >= m:
            res += (n - 1) * n * (a // m) // 2
            a %= m
            if b >= m:
                res += n * (b // m)
                b %= m
                y_max = (a * n + b) // m
                x_max = y_max * m - b
                if y_max == 0:
                    break
                res += (n - (x_max + a - 1) // a) * y_max
                n, m, a, b = (
                    y_max,
                    a,
                    m,
                    (a - x_max % a) % a,
                )
                return res


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
        a = int(input_data[ptr])
        ptr += 1
        b = int(input_data[ptr])
        ptr += 1
        m = int(input_data[ptr])
        ptr += 1
        print(floor_sum_simple(n, m, a, b))


if __name__ == "__main__":
    solve()
