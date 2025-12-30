import sys

class Solution:
    def max_repeated_block_length(self, s: str) -> int:
        n = len(s)
        MOD = 10**9 + 7
        BASE = 313
        
        def check(length):
            if length == 0: return True
            
            first_occurrence = {}
            current_hash = 0
            power = pow(BASE, length - 1, MOD)
            
            # Initial window
            for i in range(length):
                current_hash = (current_hash * BASE + ord(s[i])) % MOD
            first_occurrence[current_hash] = 0
            
            # Slide window
            for i in range(1, n - length + 1):
                remove = (ord(s[i - 1]) * power) % MOD
                current_hash = (current_hash - remove + MOD) % MOD
                current_hash = (current_hash * BASE + ord(s[i + length - 1])) % MOD
                
                if current_hash in first_occurrence:
                    if i >= first_occurrence[current_hash] + length:
                        return True
                else:
                    first_occurrence[current_hash] = i
            return False

        low, high = 0, n // 2
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

def max_repeated_block_length(s: str) -> int:
    solver = Solution()
    return solver.max_repeated_block_length(s)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    print(max_repeated_block_length(s))

if __name__ == "__main__":
    main()
