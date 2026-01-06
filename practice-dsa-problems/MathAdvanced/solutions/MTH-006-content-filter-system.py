import sys


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
        k = int(input_data[ptr])
        ptr += 1
        primes = []
        for _ in range(k):
            primes.append(int(input_data[ptr]))
            ptr += 1
            multiples = 0
            for i in range(1, 1 << k):
                lcm = 1
                cnt = 0
                for j in range(k):
                    if (i >> j) & 1:
                        cnt += 1
                        lcm *= primes[j]
                        if lcm > n:
                            break
                    else:
                        if cnt % 2 == 1:
                            multiples += n // lcm
                        else:
                            multiples -= n // lcm
                            print(n - multiples)


if __name__ == "__main__":
    solve()
