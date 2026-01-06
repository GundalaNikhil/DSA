import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    t_limit = int(input_data[ptr])
    ptr += 1
    grid = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(int(input_data[ptr]))
            ptr += 1
        grid.append(row)
        
    leaf_count = 0

    def refine(r, c, size):
        nonlocal leaf_count
        if size == 1:
            leaf_count += 1
            return
            
        v_max = -float("inf")
        v_min = float("inf")
        
        # Check range
        for i in range(r, r + size):
            row = grid[i]
            for j in range(c, c + size):
                val = row[j]
                if val > v_max: v_max = val
                if val < v_min: v_min = val
                
        if v_max - v_min <= t_limit:
            leaf_count += 1
        else:
            half = size // 2
            refine(r, c, half)
            refine(r, c + half, half)
            refine(r + half, c, half)
            refine(r + half, c + half, half)

    refine(0, 0, n)
    print(leaf_count)


if __name__ == "__main__":
    sys.setrecursionlimit(300000)
    solve()
