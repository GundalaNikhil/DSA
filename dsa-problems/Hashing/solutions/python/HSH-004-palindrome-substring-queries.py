import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

class Solution:
    def check_palindromes(self, s: str, queries: list) -> list:
        n = len(s)
        MOD = 10**9 + 7
        BASE = 313
        
        h_fwd = [0] * (n + 1)
        h_rev = [0] * (n + 1)
        power = [1] * (n + 1)
        
        rev_s = s[::-1]
        
        for i in range(n):
            h_fwd[i+1] = (h_fwd[i] * BASE + ord(s[i])) % MOD
            h_rev[i+1] = (h_rev[i] * BASE + ord(rev_s[i])) % MOD
            power[i+1] = (power[i] * BASE) % MOD
            
        def get_hash(h, l, r):
            length = r - l + 1
            return (h[r+1] - h[l] * power[length]) % MOD
            
        results = []
        for l, r in queries:
            fwd_hash = get_hash(h_fwd, l, r)
            
            rev_l = n - 1 - r
            rev_r = n - 1 - l
            rev_hash = get_hash(h_rev, rev_l, rev_r)
            
            results.append(fwd_hash == rev_hash)
            
        return results

def check_palindromes(s: str, queries: list) -> list:
    solver = Solution()
    return solver.check_palindromes(s, queries)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        s = next(iterator)
        q = int(next(iterator))
        queries = []
        for _ in range(q):
            l = int(next(iterator))
            r = int(next(iterator))
            queries.append([l, r])
            
        result = check_palindromes(s, queries)
        for ans in result:
            print("true" if ans else "false")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
