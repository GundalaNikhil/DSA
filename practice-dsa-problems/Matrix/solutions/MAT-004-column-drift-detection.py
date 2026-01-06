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
    matrix = []
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append(int(input_data[ptr]))
            ptr += 1
            matrix.append(row)
            
    for c in range(m):
        prev_adj = -float("inf")
        is_sorted = True
        for r in range(n):
            curr_adj = matrix[r][c] + r
            if curr_adj < prev_adj:
                print(c + 1) # Found drift
                return
            prev_adj = curr_adj
            
    print(0)


if __name__ == "__main__":
    solve()
