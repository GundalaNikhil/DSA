import sys

class Solution:
    def count_distinct_substrings(self, s: str) -> int:
        n = len(s)
        MOD = 10**9 + 7
        BASE = 313
        
        distinct_hashes = set()
        
        for i in range(n):
            current_hash = 0
            for j in range(i, n):
                current_hash = (current_hash * BASE + ord(s[j])) % MOD
                distinct_hashes.add(current_hash)
                
        return len(distinct_hashes) + 1

def count_distinct_substrings(s: str) -> int:
    solver = Solution()
    return solver.count_distinct_substrings(s)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    print(count_distinct_substrings(s))

if __name__ == "__main__":
    main()
