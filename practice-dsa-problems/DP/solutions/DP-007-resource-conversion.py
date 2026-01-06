import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n_days = int(input_data[ptr])
    ptr += 1
    r_types = int(input_data[ptr])
    ptr += 1
    init_q = []
    for _ in range(r_types):
        init_q.append(int(input_data[ptr]))
        ptr += 1
        c_count = int(input_data[ptr])
        ptr += 1
        conversions = []
        for _ in range(c_count):
            i = int(input_data[ptr]) - 1
            ptr += 1
            j = int(input_data[ptr]) - 1
            ptr += 1
            p = int(input_data[ptr])
            ptr += 1
            q_val = int(input_data[ptr])
            ptr += 1
            conversions.append((i, j, p, q_val))
            
    dp = {tuple(init_q)}
    
    for _ in range(n_days):
        new_dp = set()
        for state in dp:
            new_dp.add(state) # Option: Do nothing? Or is it forced?
            # Original code added existing state, so "do nothing" is valid.
            
            for i, j, p, q_val in conversions:
                if state[i] > 0:
                    new_q = list(state)
                    # Use ALL resource i? "Resource Conversion" usually implies converting batch?
                    # Code: `transfer = (new_q[i] * p) // q`
                    # `new_q[i] = 0`
                    # So it converts ALL of type i to type j.
                    transfer = (new_q[i] * p) // q_val
                    new_q[i] = 0
                    new_q[j] += transfer
                    
                    ns = tuple(new_q)
                    new_dp.add(ns)
                    
        # Pruning: Keep boolean pareto frontier?
        # Original pruner:
        # `for state in new_dp: others=state[1:], val=state[0] ... keep max(val) for others`
        # This implies we maximize index 0 resource?
        # If problem is "maximize resource 0", then yes.
        pruned = {}
        for state in new_dp:
            others = state[1:]
            if others not in pruned or state[0] > pruned[others]:
                pruned[others] = state[0]
                
        dp = set((val,) + others for others, val in pruned.items())
        
    ans = 0
    for state in dp:
        ans = max(ans, state[0])
    print(ans)


if __name__ == "__main__":
    solve()
