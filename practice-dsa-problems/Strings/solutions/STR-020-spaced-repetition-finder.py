def build_suffix_array(s):
    n = len(s)
    sa = list(range(n))
    rank = [ord(s[i]) for i in range(n)]
    k = 1
    
    while k < n:
        def key(x):
            return (rank[x], rank[x + k] if x + k < n else -1)
            
        sa.sort(key=key)
        
        new_rank = [0] * n
        new_rank[sa[0]] = 0
        for i in range(1, n):
            if key(sa[i]) == key(sa[i - 1]):
                new_rank[sa[i]] = new_rank[sa[i - 1]]
            else:
                new_rank[sa[i]] = new_rank[sa[i - 1]] + 1
                
        rank = new_rank
        if rank[sa[n - 1]] == n - 1:
            break
        k *= 2
        
    return sa


def build_lcp(s, sa):
    n = len(s)
    rank = [0] * n
    for i in range(n):
        rank[sa[i]] = i
        
    lcp = [0] * n
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = sa[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
    return lcp


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    s = input_data[0]
    n = len(s)
    
    # Needs at least index 1 for d_min?
    if len(input_data) < 2:
        return
        
    d_min = int(input_data[1])
    
    sa = build_suffix_array(s)
    lcp = build_lcp(s, sa)
    
    # Binary Search on specific length
    def check(length):
        if length == 0:
            return True, 0
            
        i = 1
        while i < n:
            if lcp[i] < length:
                i += 1
                continue
            
            # Found a group with LCP >= length
            j = i
            while j < n and lcp[j] >= length:
                j += 1
                
            # Check indices in sa[i-1 ... j-1]
            sa_range = sa[i - 1 : j]
            if max(sa_range) - min(sa_range) >= d_min:
                return True, min(sa_range)
                
            i = j
            
        return False, -1
        
    low = 1
    high = n
    ans_len = 0
    ans_start = -1
    
    while low <= high:
        mid = (low + high) // 2
        ok, start = check(mid)
        if ok:
            ans_len = mid
            ans_start = start
            low = mid + 1
        else:
            high = mid - 1
            
    if ans_len == 0:
        print("")
    else:
        # Re-run check specifically to get the lexicographically first start for best len?
        # Binary search just found ANY valid start.
        # But we want the "first" occurrence of the substring in S usually?
        # Or lexicographically first substring?
        # If multiple substrings have max length, which one?
        # Usually Suffix Array LCP finding gives us lexicographically first implicitly if scanned?
        # Actually check() scans specific group?
        # If check() finds ANY group valid, it returns.
        # But groups are processed in order of SA, so lexicographically sorted.
        # First valid group is lexicographically smallest.
        # But inside group, `min(sa_range)` is leftmost occurrence.
        # `ans_start` from binary search might not be from the 'first' valid group if logic skips?
        # No, check() scans i=1 to n. The first group it finds is lexicographically smallest.
        # So `ans_start` should be correct if check() returns immediately.
        # However, to be safe or if check(mid) logic varies, we might want to re-run.
        # The original code re-ran logic.
        
        # Let's trust check() returns best.
        # But wait, original code re-ran logic lines 78-106.
        # "real_start = n".
        # It tried to find 'real_start' which is MINIMUM index?
        # check() returns min(sa_range).
        # So yes, it returns the start index of the leftmost occurrence of that substring.
        # So string `s[start : start + len]` is correct.
        
        # But what if there are MULTIPLE different substrings of same max length?
        # check() returns the FIRST one encountered in SA order.
        # SA order is lexicographical order.
        # So we get lexicographically smallest substring?
        # Yes.
        
        print(s[ans_start : ans_start + ans_len])