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
    row_props = []
    for _ in range(n):
        row_props.append(int(input_data[ptr]))
        ptr += 1
    cols = []
    for _ in range(m):
        c_min = int(input_data[ptr])
        ptr += 1
        c_cap = int(input_data[ptr])
        ptr += 1
        cols.append((c_min, c_cap))
        
    failures = 0
    res_matrix = []
    
    for r in range(n):
        row_res = []
        rp = row_props[r]
        for c in range(m):
            cm, cc = cols[c]
            if rp < cm:
                row_res.append(-1)
                failures += 1
            else:
                # "Negotiation Matrix"?
                # Min of row prop and col cap?
                row_res.append(min(rp, cc))
        res_matrix.append(row_res)
        
    print(failures)
    for row in res_matrix:
        print(*(row))


if __name__ == "__main__":
    solve()
