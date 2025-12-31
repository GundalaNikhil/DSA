def longest_wildcard_palindrome(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0
    
    max_len = 1
    
    # Expand around each center (character and between characters)
    # 2*n - 1 centers
    for i in range(2 * n - 1):
        l = i // 2
        r = (i + 1) // 2
        
        mismatches = 0
        curr_len = 0
        
        # Determine initial match/mismatch if l != r (even length start)
        # Actually standard expansion:
        # while inside bounds:
        #   if match: expand
        #   if mismatch: 
        #      if mismatches == 0: mismatches=1, expand
        #      else: break
        
        # We need to backtrack or handle "used wildcard" state.
        # Actually, simpler:
        # Just expand and count mismatches.
        # For a fixed center, as we go out, mismatches is monotonic.
        # We want largest k such that mismatches <= 1.
        
        # Optimization:
        # We can just iterate outwards.
        
        temp_l, temp_r = l, r
        temp_mismatch = 0
        
        while temp_l >= 0 and temp_r < n:
            if s[temp_l] != s[temp_r]:
                temp_mismatch += 1
            
            if temp_mismatch > 1:
                break
                
            length = temp_r - temp_l + 1
            if length > max_len:
                max_len = length
                
            temp_l -= 1
            temp_r += 1
            
    return max_len

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