import sys

class Solution:
    def check_concatenation_equal(self, a: str, b: str, c: str, d: str) -> bool:
        if len(a) + len(b) != len(c) + len(d):
            return False

        MOD = 10**9 + 7
        BASE = 313

        def compute_hash(s):
            h = 0
            for char in s:
                h = (h * BASE + ord(char)) % MOD
            return h

        hA = compute_hash(a)
        hB = compute_hash(b)
        hC = compute_hash(c)
        hD = compute_hash(d)

        # Combine: h1 * BASE^len2 + h2
        combinedAB = (hA * pow(BASE, len(b), MOD) + hB) % MOD
        combinedCD = (hC * pow(BASE, len(d), MOD) + hD) % MOD

        return combinedAB == combinedCD

def check_concatenation_equal(a: str, b: str, c: str, d: str) -> bool:
    solver = Solution()
    return solver.check_concatenation_equal(a, b, c, d)

def main():
    lines = sys.stdin.read().split('\n')
    # Ensure we have exactly 4 lines
    while len(lines) < 4:
        lines.append("")

    a = lines[0]
    b = lines[1]
    c = lines[2]
    d = lines[3]
    result = check_concatenation_equal(a, b, c, d)
    print("true" if result else "false")

if __name__ == "__main__":
    main()
