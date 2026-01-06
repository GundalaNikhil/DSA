def count_distinct(string):
    sn = len(string)
    if sn == 0:
        return 0
        
    sa = list(range(sn))
    rank = [ord(string[i]) for i in range(sn)]
    k = 1
    
    while k < sn:
        def key(x):
            return (rank[x], rank[x + k] if x + k < sn else -1)
        
        sa.sort(key=key)
        
        new_rank = [0] * sn
        new_rank[sa[0]] = 0
        for i in range(1, sn):
            if key(sa[i]) == key(sa[i - 1]):
                new_rank[sa[i]] = new_rank[sa[i - 1]]
            else:
                new_rank[sa[i]] = new_rank[sa[i - 1]] + 1
        
        rank = new_rank
        if rank[sa[sn - 1]] == sn - 1:
            break
        k *= 2
        
    lcp = [0] * sn
    r_rank = [0] * sn
    for i in range(sn):
        r_rank[sa[i]] = i
        
    h = 0
    for i in range(sn):
        if r_rank[i] > 0:
            j = sa[r_rank[i] - 1]
            while (
                i + h < sn
                and j + h < sn
                and string[i + h] == string[j + h]
            ):
                h += 1
            lcp[r_rank[i]] = h
            if h > 0:
                h -= 1
                
    # Distinct substrings = sum( (n - sa[i]) - lcp[i] )
    total = 0
    for i in range(sn):
        total += (sn - sa[i]) - lcp[i]
        
    return total


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    s_str = list(input_data[ptr])
    ptr += 1
    q = int(input_data[ptr])
    ptr += 1
    n = len(s_str)
    
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        if op == "UPDATE":
            idx = int(input_data[ptr]) - 1
            ptr += 1
            char = input_data[ptr]
            ptr += 1
            s_str[idx] = char
        else:
            l = int(input_data[ptr]) - 1
            ptr += 1
            r = int(input_data[ptr]) - 1
            ptr += 1
            
            sub = "".join(s_str[l : r + 1])
            m = len(sub)
            
            # Constraints might be small enough for this O(M log M) logic?
            # Problem "Dynamic Substring Count" usually hard.
            # But if m <= 5000 is implied, we just run.
            
            print(count_distinct(sub))

if __name__ == "__main__":
    solve()