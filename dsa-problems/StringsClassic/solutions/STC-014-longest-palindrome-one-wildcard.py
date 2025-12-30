def longest_wildcard_palindrome(s: str) -> str:
    if not s:
        return ""
        
    T = ['^']
    for c in s:
        T.append('#')
        T.append(c)
    T.append('#')
    T.append('$')
    
    n = len(T)
    P = [0] * n
    C = 0
    R = 0
    
    for i in range(1, n - 1):
        P[i] = min(R - i, P[2 * C - i]) if R > i else 0
        
        # Expand
        while True:
            c1 = T[i + 1 + P[i]]
            c2 = T[i - 1 - P[i]]
            
            is_match = False
            if c1 == '#' or c2 == '#':
                is_match = (c1 == c2)
            elif c1 == '^' or c2 == '^' or c1 == '`' or c2 == '`':
                is_match = (c1 == c2)
            else:
                # Letters or ?
                is_match = (c1 == c2 or c1 == '?' or c2 == '?')
                
            if is_match:
                P[i] += 1
            else:
                break
                
        if i + P[i] > R:
            C = i
            R = i + P[i]
            
    max_len = 0
    center_idx = 0
    for i in range(1, n - 1):
        if P[i] > max_len:
            max_len = P[i]
            center_idx = i
            
    start = (center_idx - max_len) // 2
    return s[start : start + max_len]

def main():
    import sys
    sys.setrecursionlimit(200000)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    print(longest_wildcard_palindrome(s))

if __name__ == "__main__":
    main()