def can_rotate_to_palindrome(s: str) -> bool:
    if not s or len(s) <= 1:
        return True

    # Check all rotations
    n = len(s)
    for i in range(n):
        rotation = s[i:] + s[:i]
        if rotation == rotation[::-1]:
            return True

    return False


def main():
    import sys
    # Read input string
    input_data = sys.stdin.read().strip()
    
    # Call solution
    result = can_rotate_to_palindrome(input_data)
    
    # Output formatting: true/false
    print("true" if result else "false")

if __name__ == "__main__":
    main()
