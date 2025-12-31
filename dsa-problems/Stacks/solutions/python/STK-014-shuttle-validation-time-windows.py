def validate(push, push_t, pop, pop_t, windows, priority) -> bool:
    stack = []
    time_stack = []
    min_priority_stack = []
    
    j = 0
    n = len(push)
    
    for i in range(n):
        val = push[i]
        t = push_t[i]
        
        stack.append(val)
        time_stack.append(t)
        
        current_min = min_priority_stack[-1] if min_priority_stack else float('inf')
        if val in priority:
            current_min = min(current_min, val)
        min_priority_stack.append(current_min)
        
        while stack and j < n and stack[-1] == pop[j]:
            popped_val = stack.pop()
            pushed_time = time_stack.pop()
            min_priority_stack.pop()
            
            popped_time = pop_t[j]
            
            # Check Time Window
            if popped_val in windows:
                if popped_time - pushed_time > windows[popped_val]:
                    return False
            
            # Check Priority
            if popped_val not in priority:
                min_p = min_priority_stack[-1] if min_priority_stack else float('inf')
                if popped_val > min_p:
                    return False
            
            j += 1
            
    return not stack


def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if not lines:
        return

    num_push = int(lines[0])
    push = []
    push_t = []
    for i in range(1, num_push + 1):
        parts = lines[i].split()
        push.append(int(parts[0]))
        push_t.append(int(parts[1]))

    num_pop = int(lines[num_push + 1])
    pop = []
    pop_t = []
    for i in range(num_push + 2, num_push + 2 + num_pop):
        parts = lines[i].split()
        pop.append(int(parts[0]))
        pop_t.append(int(parts[1]))

    num_windows = int(lines[num_push + 2 + num_pop])
    windows = {}
    for i in range(num_push + 3 + num_pop, num_push + 3 + num_pop + num_windows):
        parts = lines[i].split()
        windows[int(parts[0])] = int(parts[1])

    num_priority = int(lines[num_push + 3 + num_pop + num_windows])
    priority = set()
    for i in range(num_push + 4 + num_pop + num_windows, num_push + 4 + num_pop + num_windows + num_priority):
        priority.add(int(lines[i]))

    result = validate(push, push_t, pop, pop_t, windows, priority)
    print("YES" if result else "NO")

if __name__ == "__main__":
    main()
