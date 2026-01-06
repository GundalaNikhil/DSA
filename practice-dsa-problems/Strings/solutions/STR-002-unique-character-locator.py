import sys


def solve():
    s = sys.stdin.read().strip("\r\n")
    if not s:
        return
    
    # Count frequencies
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
        
    # Find first unique char
    for char in s:
        if counts[char] == 1:
            print(char)
            return
            
    print("-1")


if __name__ == "__main__":
    solve()
