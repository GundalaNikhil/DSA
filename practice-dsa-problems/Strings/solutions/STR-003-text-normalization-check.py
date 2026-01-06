import sys


def solve():
    s = sys.stdin.read().strip("\r\n")
    
    # Filter alphanumeric and convert to lower
    filtered = []
    for char in s:
        if char.isalnum():
            filtered.append(char.lower())
            
    norm_s = "".join(filtered)
    
    # Check palindrome
    if norm_s == norm_s[::-1]:
        print("true")
    else:
        print("false")


if __name__ == "__main__":
    solve()
