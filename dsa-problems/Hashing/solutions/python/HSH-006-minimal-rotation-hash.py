import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

class Solution:
    def minimal_rotation(self, s: str) -> str:
        n = len(s)
        doubled = s + s
        m = len(doubled)
        
        MOD = 10**9 + 7
        BASE = 313
        
        h = [0] * (m + 1)
        p = [1] * (m + 1)
        
        for i in range(m):
            h[i+1] = (h[i] * BASE + ord(doubled[i])) % MOD
            p[i+1] = (p[i] * BASE) % MOD
            
        def get_hash(l, r):
            length = r - l + 1
            return (h[r+1] - h[l] * p[length]) % MOD
            
        def get_lcp(i, j):
            low, high = 0, n
            ans = 0
            while low <= high:
                mid = (low + high) // 2
                if mid == 0:
                    low = mid + 1
                    continue
                
                h1 = get_hash(i, i + mid - 1)
                h2 = get_hash(j, j + mid - 1)
                
                if h1 == h2:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
            return ans
            
        best = 0
        for curr in range(1, n):
            lcp = get_lcp(best, curr)
            if lcp < n:
                if doubled[curr + lcp] < doubled[best + lcp]:
                    best = curr
                    
        return doubled[best : best + n]

def minimal_rotation(s: str) -> str:
    solver = Solution()
    return solver.minimal_rotation(s)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    print(minimal_rotation(s))

if __name__ == "__main__":
    main()
