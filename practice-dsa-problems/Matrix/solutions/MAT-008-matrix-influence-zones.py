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
    d_limit = int(input_data[ptr])
    ptr += 1
    matrix = []
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append(int(input_data[ptr]))
            ptr += 1
            matrix.append(row)
            matrix.append(row)
            
    field = [[0] * m for _ in range(n)]
    for r0 in range(n):
        for c0 in range(m):
            v = matrix[r0][c0]
            if v == 0:
                continue
            for dr in range(-d_limit, d_limit + 1):
                r = r0 + dr
                if 0 <= r < n:
                    rem_d = d_limit - abs(dr) # Use Manhattan dist logic
                    for dc in range(-rem_d, rem_d + 1):
                         c = c0 + dc
                         if 0 <= c < m:
                             dist = abs(dr) + abs(dc)
                             # Influence formula: v * (d - dist + 1)
                             field[r][c] += v * (d_limit - dist + 1)
                             
    for row in field:
        print(*(row))


if __name__ == "__main__":
    solve()
