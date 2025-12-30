import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

def has_one_turn_path(n: int, values: list[int], left: list[int], right: list[int], target: int) -> bool:
    if n == 0:
        return False
        
    found = False
    
    def check_right_chain(u, turn_left_sum, prefixes):
        nonlocal found
        curr = u
        current_right_sum = 0
        while curr != -1 and not found:
            current_right_sum += values[curr]
            # needed_prefix = turn_left_sum + current_right_sum - target
            needed = turn_left_sum + current_right_sum - target
            if needed in prefixes:
                found = True
                return
            curr = right[curr]

    def dfs(u, current_left_sum, prefixes, is_start):
        nonlocal found
        if u == -1 or found:
            return
            
        val = values[u]
        next_sum = current_left_sum + val
        
        # If not start, we can turn
        if not is_start:
            check_right_chain(right[u], next_sum, prefixes)
            
        if found: return
        
        # Continue Left
        prefixes.add(current_left_sum)
        dfs(left[u], next_sum, prefixes, False)
        prefixes.remove(current_left_sum)
        
        if found: return
        
        # Go Right (Start new Left chain)
        dfs(right[u], 0, set(), True)

    dfs(0, 0, set(), True)
    return found

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    values = [0] * n
    left = [0] * n
    right = [0] * n
    for i in range(n):
        values[i] = int(data[idx]); idx += 1
        left[i] = int(data[idx]); idx += 1
        right[i] = int(data[idx]); idx += 1
    target = int(data[idx]) if idx < len(data) else 0
    
    print("true" if has_one_turn_path(n, values, left, right, target) else "false")

if __name__ == "__main__":
    main()
