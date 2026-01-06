import sys


def solve():
    input_data = sys.stdin.read().split()
    if len(input_data) < 3:
        return
    t = input_data[0]
    p = input_data[1]
    x_limit = int(input_data[2])
    if len(p) > len(t):
        print("false")
        return
    
    # Logic: Check if we can form p from t by deleting at most x_limit characters from p.
    # i.e., Length of Longest Common Subsequence (limited to subsequence of t) >= len(p) - x_limit.
    # Since we want p to be a subsequence of t (order matters), we just greedily match p in t.
    # Count how many chars of p we can match.
    
    matched_count = 0
    p_idx = 0
    for char in t:
        if p_idx < len(p) and char == p[p_idx]:
            matched_count += 1
            p_idx += 1
            
    if len(p) - matched_count <= x_limit:
        print("true")
    else:
        print("false")


if __name__ == "__main__":
    solve()
