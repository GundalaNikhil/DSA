import sys

class Solution:
    def longest_palindromic_prefix(self, s: str, c: str) -> int:
        T = s + c
        n = len(T)

        MOD = 10**9 + 7
        BASE = 313

        fwd_hash = 0
        rev_hash = 0
        power = 1

        max_len = 0

        for i in range(n):
            val = ord(T[i])

            fwd_hash = (fwd_hash * BASE + val) % MOD
            rev_hash = (rev_hash + val * power) % MOD

            if fwd_hash == rev_hash:
                max_len = i + 1

            power = (power * BASE) % MOD

        return max_len

def longest_palindromic_prefix(s: str, c: str) -> int:
    solver = Solution()
    return solver.longest_palindromic_prefix(s, c)

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if len(lines) < 1:
        return
    s = lines[0] if len(lines) > 0 else ''
    c = lines[1] if len(lines) > 1 else ''
    print(longest_palindromic_prefix(s, c))

if __name__ == "__main__":
    main()
