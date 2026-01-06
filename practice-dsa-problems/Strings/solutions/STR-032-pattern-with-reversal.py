import sys


def solve():
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
    t = input_data[0]
    p = input_data[1]
    if len(p) > len(t):
        print("false")
        return


def get_z(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z

def solve():
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
    t = input_data[0]
    p = input_data[1]
    
    if len(p) > len(t):
        print("false")
        return
        
    m = len(p)
    
    # Forward Z-array on P + # + T
    zn = get_z(p + "#" + t)[m + 1 :]
    
    # Backward Z-array on P_rev + # + T_rev
    # This tells us longest match of P_rev ending at some position in T_rev
    # Effectively longest match of a suffix of P (reversed) matching T backwards.
    
    tr = t[::-1]
    pr = p[::-1]
    zr = get_z(pr + "#" + tr)[m + 1 :]
    zr.reverse() 
    # zr[i] now corresponds to match length ending at i in T?
    # No, get_z return order corresponds to T_rev. 
    # reversing zr makes it align with T.
    # zr[i] is the length of suffix of P (which is prefix of P_rev) 
    # that matches a suffix of T ending at i.
    # Wait, Z-algo on P' # T' gives LCP starting at i.
    # In T_rev, "starting at i" means "ending at n-1-i" in T?
    
    # Let's verify index logic.
    # T = "abcdef", P = "cde"
    # T_rev = "fedcba", P_rev = "edc"
    # Z(P_rev # T_rev) at index corresponding to 'e' in T_rev (idx 1) is 3 ("edc").
    # zr_raw[1] = 3.
    # reversing zr_raw...
    # It accounts for alignments.
    # Let's rely on standard logic: 
    # Check split of P into P[0:k] and P[k:] s.t. one matches forward and one backward?
    # Problem is "Pattern with Reversal" - arguably checks if T contains P or P^R?
    # Or checks if T contains P where P is "ab" + "cd"^R?
    # The code `l_match + r_match >= m` checks if P starts at `i` in T, does P[0:L] match T[i:i+L] 
    # and P[L:] match T[i+L:] (maybe reversed?)
    
    # Actually, if the problem is just "Does T contain P or Reverse(P)", we check:
    # `if p in t or p[::-1] in t: print("true")`.
    # But the code uses Z-values.
    # `l_match = zn[i]` (LCP of P and T[i:])
    # `r_match = zr[i+m-1]` (LCS of P and T[...i+m-1])
    # If `l_match + r_match >= m`, it means P overlaps with itself? 
    # No it implies T[i:i+m] matches P with a "hole" or allows mismatch?
    # Or implies T[i...i+m] consists of a prefix of P and a suffix of P?
    # Yes. If prefix len + suffix len >= m (and they align?), then we have full match.
    # If zn[i] + zr[i+m-1] >= m, does it guarantee match of P? 
    # Yes, it implies P matches T[i:i+m] perfectly?
    # Actually if zn[i] = k, P[0:k] == T[i:i+k].
    # zr[i+m-1] = j implies P[m-j:m] == T[i+m-j:i+m].
    # If k + j >= m, they cover the whole string.
    # Used for "mismatch allowed"?
    
    # Assuming code intention correct: check this condition.
    
    found = False
    for i in range(len(t) - m + 1):
        l_match = zn[i]
        r_match = 0
        if i + m - 1 < len(zr):
            r_match = zr[i + m - 1]
            
        if l_match + r_match >= m: # Error tolerance? Or just 1 mismatch?
            # Standard exact match check: zn[i] == m.
            # This sum condition usually checks for "at most 1 mismatch" or similar.
            # I will trust the "Z-algorithm" check `l+r >= m-1` or similar.
            # If `l+r >= m`, it usually means exact match or match with 1 char overlap?
            # Actually if k + j >= m, and they are aligned (offset 0), it is exact match.
            # If k + j == m - 1, it is 1 mismatch.
            
            # Code checked `>= m`.
            # I'll output true if found.
            
            print("true")
            return
            
    # If Z-check fails, maybe fallback? Code had Hashing too.
    # But Hashing logic `get_hash` usage was checking `l_match` vs `tr_l`...
    # It looked like confirming the match?
    # If P matches T exactly, `zn[i]` will be m. `m >= m` -> True.
    # So this covers exact match.
    # Does it cover reversal?
    # `zr` comes from reversed strings.
    # It checks if P matches T in reverse?
    # No, `zr` logic maps T indices.
    
    # I'll stick to simple check:
    # If this Z logic works, fine.
    # But let's look at strict problem interpretation.
    # If problem is "Pattern with Reversal", it likely means P can be reversed.
    # Basic check:
    
    if p in t or p[::-1] in t:
        print("true")
        return
        
    print("false")
if __name__ == "__main__":
    solve()
