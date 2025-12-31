import sys

class Solution:
    def detect_period(self, s: str) -> int:
        n = len(s)
        MOD = 10**9 + 7
        BASE = 313
        
        h = [0] * (n + 1)
        p = [1] * (n + 1)
        
        for i in range(n):
            h[i+1] = (h[i] * BASE + ord(s[i])) % MOD
            p[i+1] = (p[i] * BASE) % MOD
            
        def get_hash(l, r):
            length = r - l + 1
            return (h[r+1] - h[l] * p[length]) % MOD
            
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
        divisors.sort()
        
        for length in divisors:
            if length == n:
                return n
            
            # Check s[0...n-length-1] == s[length...n-1]
            h1 = get_hash(0, n - length - 1)
            h2 = get_hash(length, n - 1)
            
            if h1 == h2:
                return length
                
        return n

def detect_period(s: str) -> int:
    solver = Solution()
    return solver.detect_period(s)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    print(detect_period(s))

if __name__ == "__main__":
    main()
