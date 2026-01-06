def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
        
    try:
        n_raw = int(input_data[0])
    except ValueError:
        return
        
    raw_strings = [line.strip() for line in input_data[1 : n_raw + 1]]
    if not raw_strings:
        return

    # Filter out strings that are substrings of others
    filtered = []
    for i in range(len(raw_strings)):
        is_sub = False
        for j in range(len(raw_strings)):
            if i != j and raw_strings[i] in raw_strings[j]:
                # If identical, only eliminate higher index (keep one copy)
                if len(raw_strings[i]) < len(raw_strings[j]):
                    is_sub = True
                    break
                elif len(raw_strings[i]) == len(raw_strings[j]) and i > j:
                     is_sub = True
                     break
                     
        if not is_sub:
            filtered.append(raw_strings[i])
            
    n = len(filtered)
    if n == 0:
        print("")
        return
        
    # Precompute overlaps
    # overlaps[i][j] = length of suffix of filtered[i] that matches prefix of filtered[j]
    overlaps = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j: 
                continue
            s1, s2 = filtered[i], filtered[j]
            # Try to match suffix of s1 with prefix of s2
            # Max overlap length is min(len(s1), len(s2)) - 1? Or can be full if substring?
            # We already removed substrings. So overlap must be strict < len(min).
            for k in range(min(len(s1), len(s2)), 0, -1):
                if s1.endswith(s2[:k]):
                    overlaps[i][j] = k
                    break
                    
    # TSP DP
    # dp[mask][last_idx] = (length, reconstructed_string)
    # Reconstructing string might be memory heavy (O(2^N * N * L)).
    # Better to store parent pointers if N is up to 15-20.
    # But usually N <= 12-15 for string TSP.
    # Code used reconstructing string. I will stick to it if N logic supports it.
    
    dp = [[(float("inf"), "")] * n for _ in range(1 << n)]
    
    # Init base cases
    for i in range(n):
        dp[1 << i][i] = (len(filtered[i]), filtered[i])
        
    for mask in range(1, 1 << n):
        for i in range(n):
            if mask & (1 << i):
                curr_len, curr_str = dp[mask][i]
                if curr_len == float("inf"):
                    continue
                    
                # Try to append j
                for j in range(n):
                    if not (mask & (1 << j)):
                        next_mask = mask | (1 << j)
                        overlap = overlaps[i][j]
                        added = filtered[j][overlap:]
                        new_len = curr_len + len(added)
                        new_str = curr_str + added
                        
                        best_len, best_str = dp[next_mask][j]
                        
                        if new_len < best_len:
                            dp[next_mask][j] = (new_len, new_str)
                        elif new_len == best_len:
                            if new_str < best_str:
                                dp[next_mask][j] = (new_len, new_str)
                                
    # Final answer
    ans_len = float("inf")
    ans_str = ""
    final_mask = (1 << n) - 1
    
    for i in range(n):
        l, s = dp[final_mask][i]
        if l < ans_len:
            ans_len = l
            ans_str = s
        elif l == ans_len:
            if s < ans_str:
                ans_str = s
                
    print(ans_str)

if __name__ == "__main__":
    solve()