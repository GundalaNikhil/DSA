import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    sizes = []
    for _ in range(n):
        sizes.append(int(input_data[ptr]))
        ptr += 1
        join_matrix = []
        for _ in range(n):
            row = []
            for _ in range(n):
                row.append(int(input_data[ptr]))
                ptr += 1
                join_matrix.append(row)
                join_matrix.append(row)
                
    inf = float("inf")
    dp = [inf] * (1 << n)
    subset_size = [0] * (1 << n)
    
    # Precalc sizes
    for mask in range(1, 1 << n):
        s = 0
        for i in range(n):
            if (mask >> i) & 1:
                s += sizes[i]
        subset_size[mask] = s
        
    # Init single tables (cost 0)
    for i in range(n):
        dp[1 << i] = 0
        
    # DP
    for mask in range(1, 1 << n):
        if bin(mask).count("1") < 2:
            continue
            
        # Iterate submasks
        sub = (mask - 1) & mask
        while sub > 0:
            if sub > (mask ^ sub): # Avoid duplicates (A, B) vs (B, A)? Wait, symmetrical?
                # Code: `if sub > (mask ^ sub)`. Yes.
                A = sub
                B = mask ^ sub
                
                # Join cost between A and B
                jc = 0
                for i in range(n):
                    if (A >> i) & 1:
                        for j in range(n):
                            if (B >> j) & 1:
                                jc += join_matrix[i][j]
                                
                cost = (
                    dp[A]
                    + dp[B]
                    + subset_size[A] * subset_size[B] # Simple cost model: product of sizes?
                    + jc
                )
                
                if cost < dp[mask]:
                    dp[mask] = cost
            sub = (sub - 1) & mask
            
    print(dp[(1 << n) - 1])
