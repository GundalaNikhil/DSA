import sys
from itertools import permutations


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    cr = int(input_data[ptr])
    ptr += 1
    cc = int(input_data[ptr])
    ptr += 1
    cs = int(input_data[ptr])
    ptr += 1
    a = []
    for _ in range(n):
        a.append([int(x) for x in input_data[ptr : ptr + m]])
        ptr += m
        
    b = []
    for _ in range(n):
        b.append([int(x) for x in input_data[ptr : ptr + m]])
        ptr += m
        
    def count_swaps(p):
        n_p = len(p)
        visited = [False] * n_p
        cycles = 0
        for i in range(n_p):
            if not visited[i]:
                cycles += 1
                curr = i
                while not visited[curr]:
                    visited[curr] = True
                    curr = p[curr]
        return n_p - cycles

    min_total_cost = float("inf")
    row_perms = list(permutations(range(n)))
    col_perms = list(permutations(range(m)))
    
    for rp in row_perms:
        r_swaps = count_swaps(rp)
        r_cost = r_swaps * cr
        for cp in col_perms:
            c_swaps = count_swaps(cp)
            c_cost = c_swaps * cc
            cell_cost = 0
            
            # Optimization: could break early if cost > min
            for i in range(n):
                for j in range(m):
                    if a[rp[i]][cp[j]] != b[i][j]:
                        cell_cost += cs
                        
            min_total_cost = min(min_total_cost, r_cost + c_cost + cell_cost)
            
    print(min_total_cost)


if __name__ == "__main__":
    solve()
