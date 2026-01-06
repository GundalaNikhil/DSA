import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    weights = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(int(input_data[ptr]))
            ptr += 1
            weights.append(row)
            forbid = []
            for _ in range(n):
                row = []
                for _ in range(n):
                    row.append(int(input_data[ptr]))
                    ptr += 1
                forbid.append(row)
            
    num_masks = 1 << n
    inf = float("inf")
    dp = [[-inf] * n for _ in range(num_masks)]
    
    # Init: single item masks
    for i in range(n):
        dp[1 << i][i] = weights[i][0]
        
    for mask in range(1, num_masks):
        pos = bin(mask).count("1")
        if pos == n:
            continue
            
        # Try to extend mask
        # Existing state: mask, last added item `last`
        for last in range(n):
            if dp[mask][last] == -inf:
                continue
                
            for next_val in range(n):
                if not (mask & (1 << next_val)):
                    # Check constraints
                    if forbid[last][next_val] == 0:
                        new_mask = mask | (1 << next_val)
                        # We are adding item `next_val` at position `pos` (0-indexed?)
                        # Original: `weights[next_val][pos]`.
                        # If mask has 1 bit, pos=1. We add 2nd item at index 1. Correct.
                        
                        dp[new_mask][next_val] = max(
                            dp[new_mask][next_val],
                            dp[mask][last] + weights[next_val][pos],
                        )
                        
    ans = max(dp[num_masks - 1])
    print(ans if ans != -inf else -1)


if __name__ == "__main__":
    solve()
