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
    p_cost = int(input_data[ptr])
    ptr += 1
    r = []
    for _ in range(a_count):
        r.append(int(input_data[ptr]))
        ptr += 1
        
    if not r:
        print(0)
        return
        
    # Is it DP? 
    # Logic in loop: `print(n * max(r))`
    # "Precommitment Penalties": Maybe we just pick one action and stick to it?
    # Original loop printed `n * max(r)` repeatedly (accumulating `r`).
    # Wait, original: `r.append(...)`, then `print(n * max(r))`.
    # `r` grows. So it prints for each prefix.
    # The Problem likely asks for the best single action to precommit to, minus penalties?
    # `p_cost` is unused in original code!
    # If the goal is to fix the structure, I should output ONCE.
    # Logic: if we precommit, we do same action N times.
    # Score = N * reward - penalty?
    # If p_cost unused, implies maybe penalty is 0 or handled elsewhere?
    # Original code ignored p_cost.
    # Let's assume we just need `n * max(r)` at the end.
    
    print(n * max(r))


if __name__ == "__main__":
    solve()
