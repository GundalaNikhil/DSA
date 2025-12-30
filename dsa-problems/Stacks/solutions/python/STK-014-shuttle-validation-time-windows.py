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
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
