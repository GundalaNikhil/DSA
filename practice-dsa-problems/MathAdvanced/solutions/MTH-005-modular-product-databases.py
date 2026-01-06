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
    out = []
    for _ in range(q):
        l = int(input_data[ptr])
        ptr += 1
        r = int(input_data[ptr])
        ptr += 1
        if l == 0:
            out.append("0")
            continue
        if r - l < 10000:
            res = 1
            for i in range(l, r + 1):
                res = (res * i) % p
                out.append(str(res))
            else:
                if p - r < 10000:
                    denom = 1
                    for i in range(r + 1, p):
                        denom = (denom * i) % p
                        r_fact = (p - 1) * pow(denom, p - 2, p) % p
                        pass
                    res = 1
                    for i in range(l, r + 1):
                        res = (res * i) % p
                        out.append(str(res))
                        sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    solve()
