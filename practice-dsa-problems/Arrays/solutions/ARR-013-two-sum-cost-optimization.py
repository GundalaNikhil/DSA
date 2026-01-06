import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        t_sum = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))
        c = []
        for _ in range(n):
            c.append(int(next(iterator)))
    except StopIteration:
        return
        
    best_at = {} # val -> (cost, index)
    best_total_cost = float("inf")
    best_pair = None
    
    for j in range(n):
        val_j = a[j]
        cost_j = c[j]
        val_i = t_sum - val_j
        
        if val_i in best_at:
            cost_i, i_idx = best_at[val_i]
            total_cost = cost_i + cost_j
            
            curr_pair = (i_idx + 1, j + 1)
            
            if total_cost < best_total_cost:
                best_total_cost = total_cost
                best_pair = curr_pair
            elif total_cost == best_total_cost:
                if best_pair is None or curr_pair < best_pair:
                    best_pair = curr_pair
                    
        if val_j not in best_at or cost_j < best_at[val_j][0]:
            best_at[val_j] = (cost_j, j)
            
    if best_pair:
        print(f"{best_pair[0]} {best_pair[1]}")
    else:
        print("-1")

if __name__ == "__main__":
    solve()
