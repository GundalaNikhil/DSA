def prev_greater_opposite_parity(arr: list[int]) -> list[int]:
    n = len(arr)
    result = [-1] * n
    
    even_stack = [] # Indices
    odd_stack = []  # Indices
    
    def find_nearest_greater(stack, val):
        # Stack has indices of decreasing values: [Big ... Small]
        # We want the rightmost element in stack > val
        # This corresponds to the smallest valid value in the stack
        if not stack:
            return -1
            
        l, r = 0, len(stack) - 1
        ans_idx = -1
        
        while l <= r:
            mid = (l + r) // 2
            if arr[stack[mid]] > val:
                ans_idx = stack[mid]
                l = mid + 1 # Try closer (right)
            else:
                r = mid - 1
        return ans_idx
        
    for i, val in enumerate(arr):
        if val % 2 == 0:
            # Look in Odd
            idx = find_nearest_greater(odd_stack, val)
            if idx != -1:
                result[i] = arr[idx]
            
            # Update Even
            while even_stack and arr[even_stack[-1]] <= val:
                even_stack.pop()
            even_stack.append(i)
        else:
            # Look in Even
            idx = find_nearest_greater(even_stack, val)
            if idx != -1:
                result[i] = arr[idx]
                
            # Update Odd
            while odd_stack and arr[odd_stack[-1]] <= val:
                odd_stack.pop()
            odd_stack.append(i)
            
    return result


def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if not lines:
        return

    n = int(lines[0])
    arr = list(map(int, lines[1].split()))
    result = prev_greater_opposite_parity(arr)
    for r in result:
        print(r)

if __name__ == "__main__":
    main()
