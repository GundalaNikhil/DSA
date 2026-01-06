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
    actions = []
    for _ in range(a_count):
        actions.append((int(input_data[ptr]), int(input_data[ptr + 1])))
        ptr += 2
        
    best_r = -float("inf")
    best_f = float("inf")
    
    # Pareto frontier: Maximize R, Minimize F?
    # Logic:
    # If r > best_r: update both.
    # If r == best_r: if f < best_f: update f.
    # This finds the single action with Max R, and Min F among those.
    # Is it DP? "Multi-objective".
    # Just single pass linear scan.
    
    for r, f in actions:
        if r > best_r:
            best_r = r
            best_f = f
        elif r == best_r:
            if f < best_f:
                best_f = f
                
    if best_r != -float("inf"):
        print(n * best_r, n * best_f)
    else:
        print(0, 0)


if __name__ == "__main__":
    solve()
