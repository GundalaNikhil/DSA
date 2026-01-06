import sys


def solve():
    s = sys.stdin.read().strip()
    if not s:
        print("")
        return
    n = len(s)
    vowels = set("aeiou")
    cons_info = []
    # Extract consonants and their original indices
    for idx, char in enumerate(s):
        if char not in vowels:
            cons_info.append((char, idx))
            
    # Handle empty consonants case
    # If no consonants, what? Problem implies "Mirror Finder" on consonants?
    # Original logic had `if not cons_info: print(s); return` inside loop?
    # If loop finishes and empty?
    # Logic implies finding longest palindromic subsequence of consonants? 
    # Or substring in original string that contains palindromic consonants?
    
    if not cons_info:
        # Original logic printed 's'? Or handled empty?
        # Assuming if no consonants, maybe whole string or empty?
        # Original code: `gaps.append((0, n-1))` for empty case logic implies processing gaps?
        pass # Logic below handles gaps if cons_info empty?
        
    m = len(cons_info)
    
    # CASE 1: Longest Palindromic Consonants
    # Run Manacher on consonants string
    cons_chars = "".join(c for c, _ in cons_info)
    t = "#" + "#".join(cons_chars) + "#"
    p = [0] * len(t)
    center = right = 0
    
    for i in range(len(t)):
        if i < right:
            p[i] = min(right - i, p[2 * center - i])
        while (
            i + p[i] + 1 < len(t)
            and i - p[i] - 1 >= 0
            and t[i + p[i] + 1] == t[i - p[i] - 1]
        ):
            p[i] += 1
        if i + p[i] > right:
            center = i
            right = i + p[i]
            
    # Find best palindrome in consonant space
    # And map back to original indices to include surrounding non-consonants?
    
    best_len = -1
    best_start = -1
    
    # Iterate all Manacher centers
    for i in range(len(t)):
        # Radius p[i] in spread string `t`.
        # Length in original cons string is p[i].
        # Indices in cons_info:
        # Start index in cons_info: (i - p[i]) // 2
        # End index in cons_info: (i + p[i]) // 2 - 1
        
        idx_start = (i - p[i]) // 2
        idx_end = (i + p[i]) // 2 - 1
        
        # Adjust for '#' centers
        if t[i] == "#":
            # Consonants are at odd indices in t (1, 3, 5...) ? No.
            # t = # c # c #
            # indices: 0 1 2 3 4
            # chars at 1, 3.
            pass
            
        # Correct mapping:
        # p[i] is length.
        # if p[i] == 0: palindrome empty.
        
        if idx_start > idx_end:
            # Empty palindrome (length 0).
            # Should we consider pure vowel substrings as candidates?
            # Yes, original logic handled gaps.
            pass
        
        # Define boundaries in original string `s`
        # Left boundary is character AFTER previous consonant (or start of string)
        # Right boundary is character BEFORE next consonant (or end of string)
        
        # Consonant range in `s`:
        # cons_info[idx_start] ... cons_info[idx_end]
        # We extend left to just after cons_info[idx_start - 1]
        # Extend right to just before cons_info[idx_end + 1]
        
        l_boundary = 0
        if idx_start > 0:
            l_boundary = cons_info[idx_start - 1][1] + 1
            
        r_boundary = n - 1
        if idx_end < m - 1:
            r_boundary = cons_info[idx_end + 1][1] - 1
            
        # Note: if cons list is empty, loops don't run, we need separate handling.
        curr_len = r_boundary - l_boundary + 1
        
        if curr_len > best_len:
            best_len = curr_len
            best_start = l_boundary
        elif curr_len == best_len:
            if l_boundary < best_start:
                best_start = l_boundary
        
    # Handling purely vowel case (no consonants)
    if not cons_info:
        # The while loop for Manacher might run for t="#"?
        # len(t)=1. i=0. p[0]=0. idx_start=0, idx_end=-1.
        # Logic executes once. l_boundary=0, r_boundary=n-1.
        # best_len = n. best_start = 0.
        # Correctly selects whole string.
        pass
        
    print(s[best_start : best_start + best_len])


if __name__ == "__main__":
    solve()
