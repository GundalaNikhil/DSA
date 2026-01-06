import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    q = int(input_data[ptr])
    ptr += 1
    best_prio = [-1.0] * (n * m)
    best_time = [float("inf")] * (n * m)
    best_area = [-1] * (n * m)
    best_id = [float("inf")] * (n * m)
    current_owner = [0] * (n * m)
    ans = []
    for i in range(1, q + 1):
        r1 = int(input_data[ptr])
        ptr += 1
        c1 = int(input_data[ptr])
        ptr += 1
        r2 = int(input_data[ptr])
        ptr += 1
        c2 = int(input_data[ptr])
        ptr += 1
        prio = float(input_data[ptr])
        ptr += 1
        time = float(input_data[ptr])
        ptr += 1
        area = (r2 - r1 + 1) * (c2 - c1 + 1)
        count = 0
        
        # This problem needs a count of "owned" cells?
        # Or count of updates?
        # The original code tracks `count`.
        # `count += 1` inside `if better`.
        # So it counts how many cells changed ownership in this query?
        
        for r in range(r1 - 1, r2):
            offset = r * m
            for c in range(c1 - 1, c2):
                idx = offset + c
                better = False
                
                # Comparison logic
                if prio > best_prio[idx]:
                    better = True
                elif prio == best_prio[idx]:
                    if time < best_time[idx]:
                        better = True
                    elif time == best_time[idx]:
                        if area > best_area[idx]:
                            better = True
                        elif area == best_area[idx]:
                            if i < best_id[idx]:
                                better = True
                                
                if better:
                    best_prio[idx] = prio
                    best_time[idx] = time
                    best_area[idx] = area
                    best_id[idx] = i
                    current_owner[idx] = i
                    count += 1
                    
        ans.append(str(count))
        
    sys.stdout.write("\n".join(ans) + "\n")
    # Output final grid ownership?
    # Original printed it after every update inside the loop? 
    # That would be insanely huge output.
    # Usually output result after all queries? Or grid only at end?
    # Given typical problem formats, grid at end makes sense.
    
    for r in range(n):
        print(*(current_owner[r * m : (r + 1) * m]))


if __name__ == "__main__":
    solve()
