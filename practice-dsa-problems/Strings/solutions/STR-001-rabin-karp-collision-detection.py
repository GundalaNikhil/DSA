import sys


def solve():
    lines = sys.stdin.readlines()
    if len(lines) < 2:
        return
    t_str = lines[0].strip()
    p_str = lines[1].strip()
    n = len(t_str)
    m = len(p_str)
    if m > n:
        print("0 0")
        return
    mod1 = 1000000007
    mod2 = 1000000009
    base = 911382323
    
    # 1. Compute Pattern Hash
    h1_p = 0
    h2_p = 0
    for char in p_str:
        val = ord(char) - ord("a") + 1
        h1_p = (h1_p * base + val) % mod1
        h2_p = (h2_p * base + val) % mod2

    # 2. Precompute powers
    pow1 = pow(base, m, mod1)
    pow2 = pow(base, m, mod2)
    
    # 3. Rolling Hash on Text
    h1_t = 0
    h2_t = 0
    
    # Initial window hash (first m chars)
    # Actually, let's do standard rolling. 
    # We can iterate i from 0 to n.
    # Add new char, if i >= m remove old char.
    
    exact_matches = 0
    false_hash_matches = 0
    
    for i in range(n):
        val = ord(t_str[i]) - ord("a") + 1
        h1_t = (h1_t * base + val) % mod1
        h2_t = (h2_t * base + val) % mod2
        
        if i >= m:
            prev_val = ord(t_str[i - m]) - ord("a") + 1
            # Rolling update: remove leading character
            # Standard formula: hash = (hash - val * base^m) % mod
            # But wait, usually we multiply by base at each step.
            # So the term to remove is prev_val * base^m.
            # However, indices:
            # Current char at i added as * base^0 (units place)? No, usually * base + new_val.
            # So current char is at units place.
            # Char at i-m was added m steps ago, so it has factor base^m.
            
            h1_t = (h1_t - prev_val * pow1) % mod1
            h2_t = (h2_t - prev_val * pow2) % mod2
            
            # Correction for negative modulo result
            if h1_t < 0: h1_t += mod1
            if h2_t < 0: h2_t += mod2

        # Check match if window is full length m
        # We have processed characters up to i. Length is i + 1.
        # We need length >= m. (i >= m - 1)
        
        if i >= m - 1:
            if h1_t == h1_p and h2_t == h2_p:
                # Potential match
                if t_str[i - m + 1 : i + 1] == p_str:
                    exact_matches += 1
                else:
                    false_hash_matches += 1

    print(f"{exact_matches} {false_hash_matches}")


if __name__ == "__main__":
    solve()


if __name__ == "__main__":
    solve()
