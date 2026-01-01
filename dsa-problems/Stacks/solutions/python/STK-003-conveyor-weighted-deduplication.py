def reduce_stack(s: str, w: list[int]) -> tuple[str, int]:
    stack = [] # List of tuples (char, weight)
    total_removed = 0
    
    for char, weight in zip(s, w):
        # Check adjacent duplicate with even sum
        if stack and stack[-1][0] == char and (stack[-1][1] + weight) % 2 == 0:
            total_removed += stack[-1][1] + weight
            stack.pop()
        else:
            stack.append((char, weight))
            
    reduced_s = "".join(item[0] for item in stack)
    return reduced_s, total_removed


def main():
    import sys
    # Read all lines
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        chars = []
        weights = []
        for _ in range(n):
            chars.append(next(iterator))
            weights.append(int(next(iterator)))
        
        s = "".join(chars)
        
        res_s, res_removed = reduce_stack(s, weights)
        
        if not res_s:
            print(f"EMPTY {res_removed}")
        else:
            print(f"{res_s} {res_removed}")
            
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
