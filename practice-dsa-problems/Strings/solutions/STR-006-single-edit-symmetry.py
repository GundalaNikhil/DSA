import sys


def is_palindrome(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


def solve():
    s = sys.stdin.read().strip()
    if not s:
        print("true")
        return
    
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            # Try deleting left or right character
            if is_palindrome(s, l + 1, r) or is_palindrome(s, l, r - 1):
                print("true")
                return
            else:
                print("false")
                return
        l += 1
        r -= 1
        
    print("true")


if __name__ == "__main__":
    solve()
