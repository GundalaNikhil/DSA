import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    p_size = int(input_data[ptr])
    ptr += 1
    n_len = int(input_data[ptr])
    ptr += 1
    pop = {}
    sums = {}
    
    for i in range(1, p_size + 1):
        lst = []
        s = 0
        for _ in range(n_len):
            val = int(input_data[ptr])
            ptr += 1
            lst.append(val)
            s += val
        pop[i] = lst
        sums[i] = s
        
    q = int(input_data[ptr])
    ptr += 1
    mid = n_len // 2
    
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        
        if op == "CROSS":
            id1 = int(input_data[ptr])
            ptr += 1
            id2 = int(input_data[ptr])
            ptr += 1
            new_lst = pop[id1][:mid] + pop[id2][mid:]
            pop[id1] = new_lst
            sums[id1] = sum(new_lst)
        elif op == "MUTATE":
            id_a = int(input_data[ptr])
            ptr += 1
            pos = int(input_data[ptr])
            ptr += 1
            x = int(input_data[ptr])
            ptr += 1
            idx = pos - 1
            # Assuming idx is valid
            if 0 <= idx < n_len:
                old_val = pop[id_a][idx]
                pop[id_a][idx] = x
                sums[id_a] = sums[id_a] - old_val + x
                
        # Calculate best fitness after op?
        # The logic was nested inside MUTATE but likely applies to any update?
        # Or maybe it's just a query that runs every time?
        # Original code had logic:
        # best_id = 1 ... print(best_id) inside MUTATE only?
        # If so, keep it there.
        # But check logic. It prints best_id.
        
        if op == "MUTATE" or op == "CROSS": # Assuming we print best after every op?
             # Original code only had print inside MUTATE block.
             # I will keep it consistent with original but usually genetic algo prints best every step.
             # Wait, the indentation in original was weird.
             # Everything from line 50 was inside `elif op == "MUTATE":`.
             # If CROSS happened, nothing printed?
             # Let's assume it should print every time if that's the intention, but if strictly follows original flow...
             # The indentation suggests it was specific to MUTATE.
             pass
             
        if op == "MUTATE":
            best_id = 1
            max_fitness = sums[1]
            for i in range(2, p_size + 1):
                if sums[i] > max_fitness:
                    max_fitness = sums[i]
                    best_id = i
                elif sums[i] == max_fitness:
                    if i < best_id:
                        best_id = i
            print(best_id)


if __name__ == "__main__":
    solve()
