import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    row_auth = []
    for _ in range(n):
        row_auth.append(int(input_data[ptr]))
        ptr += 1
        
    col_rules = []
    for _ in range(m):
        rtype = int(input_data[ptr])
        ptr += 1
        rval = int(input_data[ptr])
        ptr += 1
        col_rules.append((rtype, rval))
        
    for r in range(n):
        row_res = []
        base = row_auth[r]
        for c in range(m):
            t, v = col_rules[c]
            if t == 0:
                # Type 0: Row base only? Or ignore col rule?
                # "Row Authority" implies row overrides?
                # Usually: 0 -> Base, 1 -> Min, 2 -> Col Val
                row_res.append(base)
            elif t == 1:
                row_res.append(min(base, v))
            elif t == 2:
                row_res.append(v)
        print(*(row_res))


if __name__ == "__main__":
    solve()
