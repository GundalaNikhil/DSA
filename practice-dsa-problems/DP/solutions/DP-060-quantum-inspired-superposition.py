import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    a_count = int(input_data[ptr])
    ptr += 1
    matrices = []
    for _ in range(a_count):
        a = int(input_data[ptr])
        ptr += 1
        b = int(input_data[ptr])
        ptr += 1
        c = int(input_data[ptr])
        ptr += 1
        d = int(input_data[ptr])
        ptr += 1

        matrices.append((a, b, c, d))
        
    dp = {(1, 0): 0}
    
    for step in range(n):
        new_dp = {}
        for (x, y), score in dp.items():
            for a, b, c, d in matrices:
                nx, ny = a * x + b * y, c * x + d * y
                
                # Superposition? Or just keeping track of vector state?
                # Code just uses (nx, ny) as state.
                
                if (nx, ny) not in new_dp or new_dp[(nx, ny)] < score:
                    new_dp[(nx, ny)] = score
                    
                # Collapse?
                # Logic: `nx, ny = (1, 0) if x >= y else (0, 1)`.
                # Wait, original code:
                # 32: `nx, ny = (1, 0) if x >= y else (0, 1)` (after previous `nx, ny` calculation, overwriting?)
                # 34: `if (nx, ny) not in new_dp ... score + rew`.
                # This seems to be a SECOND transition or option?
                # "Quantum Inspired Superposition": Maybe Apply matrix OR Collapse?
                # Original code inside loop over matrices:
                # `nx, ny = a*x...`. Update new_dp.
                # THEN `nx, ny = collapsed...`. Update new_dp.
                # Loop runs for each matrix.
                # Collapse logic depends on `x, y` (current state), not matrix?
                # So for each matrix, we try applying matrix.
                # AND we also try collapsing?
                # If collapse logic is inside matrix loop, we do it M times? Same result M times?
                # Redundant but harmless if maxing.
                # Let's preserve logic.
                
                cnx, cny = (1, 0) if x >= y else (0, 1)
                rew = 1 if x >= y else 0
                if (cnx, cny) not in new_dp or new_dp[(cnx, cny)] < score + rew:
                    new_dp[(cnx, cny)] = score + rew
                    
        dp = new_dp
        
    print(max(dp.values()) if dp else 0)


if __name__ == "__main__":
    solve()
