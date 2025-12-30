import sys

class Solution:
    def count_pairs(self, s: str, L: int) -> int:
        n = len(s)
        if L > n:
            return 0
            
        MOD1 = 10**9 + 7
        BASE1 = 313
        MOD2 = 10**9 + 9
        BASE2 = 317
        
        counts = {}
        
        h1 = 0
        h2 = 0
        p1 = pow(BASE1, L - 1, MOD1)
        p2 = pow(BASE2, L - 1, MOD2)
        
        # Initial window
        for i in range(L):
            val = ord(s[i])
            h1 = (h1 * BASE1 + val) % MOD1
            h2 = (h2 * BASE2 + val) % MOD2
            
        key = (h1, h2)
        counts[key] = 1
        
        # Slide
        for i in range(1, n - L + 1):
            val_remove = ord(s[i - 1])
            val_add = ord(s[i + L - 1])
            
            remove1 = (val_remove * p1) % MOD1
            h1 = (h1 - remove1 + MOD1) % MOD1
            h1 = (h1 * BASE1 + val_add) % MOD1
            
            remove2 = (val_remove * p2) % MOD2
            h2 = (h2 - remove2 + MOD2) % MOD2
            h2 = (h2 * BASE2 + val_add) % MOD2
            
            key = (h1, h2)
            counts[key] = counts.get(key, 0) + 1
            
        ans = 0
        for count in counts.values():
            ans += count * (count - 1) // 2
            
        return ans

def count_pairs(s: str, L: int) -> int:
    solver = Solution()
    return solver.count_pairs(s, L)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    s = input_data[0]
    if len(input_data) > 1:
        L = int(input_data[1])
        print(count_pairs(s, L))

if __name__ == "__main__":
    main()
