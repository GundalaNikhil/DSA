import sys

class Solution:
    def longest_common_substring(self, a: str, b: str) -> int:
        MOD = 10**9 + 7
        BASE = 31

        def check(length):
            if length == 0: return True

            # Compute hashes for A
            hashes_a = set()
            current_hash = 0
            power = pow(BASE, length - 1, MOD)

            for i in range(length):
                current_hash = (current_hash * BASE + ord(a[i])) % MOD
            hashes_a.add(current_hash)

            for i in range(length, len(a)):
                remove = (ord(a[i - length]) * power) % MOD
                current_hash = (current_hash - remove + MOD) % MOD
                current_hash = (current_hash * BASE + ord(a[i])) % MOD
                hashes_a.add(current_hash)

            # Check B
            current_hash = 0
            for i in range(length):
                current_hash = (current_hash * BASE + ord(b[i])) % MOD
            if current_hash in hashes_a:
                return True

            for i in range(length, len(b)):
                remove = (ord(b[i - length]) * power) % MOD
                current_hash = (current_hash - remove + MOD) % MOD
                current_hash = (current_hash * BASE + ord(b[i])) % MOD
                if current_hash in hashes_a:
                    return True

            return False

        low, high = 0, min(len(a), len(b))
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if mid == 0:
                low = mid + 1
                continue
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans

def longest_common_substring(a: str, b: str) -> int:
    solver = Solution()
    return solver.longest_common_substring(a, b)

def main():
    lines = sys.stdin.read().strip().split('\n')
    if len(lines) < 2:
        return

    a = lines[0] if len(lines) > 0 else ""
    b = lines[1] if len(lines) > 1 else ""
    print(longest_common_substring(a, b))

if __name__ == "__main__":
    main()
