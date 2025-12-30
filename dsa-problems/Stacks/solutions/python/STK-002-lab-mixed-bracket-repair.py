def can_repair(s: str) -> bool:
    n = len(s)
    if n % 2 != 0:
        return False
        
    left_stack = []
    star_stack = []
    
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for i, c in enumerate(s):
        if c in "([{":
            left_stack.append(i)
        elif c == "?":
            star_stack.append(i)
        else:
            # Closer
            if left_stack and left_stack[-1] in "([{" and s[left_stack[-1]] == pairs[c]:
                left_stack.pop()
            elif star_stack:
                star_stack.pop()
            else:
                return False
                
    while left_stack:
        if not star_stack:
            return False
        if left_stack[-1] < star_stack[-1]:
            left_stack.pop()
            star_stack.pop()
        else:
            return False
            
    return len(star_stack) % 2 == 0


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
