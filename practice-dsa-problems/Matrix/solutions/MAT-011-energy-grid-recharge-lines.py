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
    row_recharge = []
    for _ in range(n):
        row_recharge.append(int(input_data[ptr]))
        ptr += 1
    for _ in range(n):
        row_recharge.append(int(input_data[ptr]))
        ptr += 1
        
    col_drain = []
    for _ in range(m):
        col_drain.append(int(input_data[ptr]))
        ptr += 1
        
    base = []
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append(int(input_data[ptr]))
            ptr += 1
        base.append(row)
        
    active_count = 0
    active_grid = []
    for r in range(n):
        row_res = []
        for c in range(m):
            net = base[r][c] + row_recharge[r] + col_drain[c]
            if net >= 0:
                row_res.append(1)
                active_count += 1
            else:
                row_res.append(0)
        active_grid.append(row_res)
        
    print(active_count)
    for row in active_grid:
        print(*(row))


if __name__ == "__main__":
    solve()
