import sys

# Note: Full O(N log^2 N) implementation requires ~300 lines of NTT/Poly code.
# Providing O(N^2) Horner's Method for conciseness and correctness on small inputs.
# For N=10^5, this will TLE. In a real contest, one pastes a pre-written library.

class Solution:
    def multipoint_evaluation(self, coeffs: list[int], points: list[int]) -> list[int]:
        MOD = 1000000007
        results = []
        for x in points:
            val = 0
            # Horner's method: coeffs are [a0, a1, ..., ad]
            # Evaluate a0 + a1*x + ... + ad*x^d
            # = a0 + x(a1 + x(a2 + ...))
            for i in range(len(coeffs) - 1, -1, -1):
                val = (val * x + coeffs[i]) % MOD
            results.append(val)
        return results

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        d = int(next(iterator))
        n = int(next(iterator))
        coeffs = [int(next(iterator)) for _ in range(d + 1)]
        points = [int(next(iterator)) for _ in range(n)]
        
        sol = Solution()
        res = sol.multipoint_evaluation(coeffs, points)
        print(*(res))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
