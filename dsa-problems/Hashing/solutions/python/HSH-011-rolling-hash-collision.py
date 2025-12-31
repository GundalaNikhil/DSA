import sys

# Increase recursion depth
sys.setrecursionlimit(20000)

class Solution:
    def find_collision(self, B: int, M: int, L: int) -> tuple:
        seen = {}
        
        def compute_hash(s):
            h = 0
            for char in s:
                h = (h * B + ord(char)) % M
            return h
            
        def dfs(current_s):
            if len(current_s) == L:
                h = compute_hash(current_s)
                if h in seen:
                    return (seen[h], current_s)
                seen[h] = current_s
                return None
            
            for char_code in range(ord('a'), ord('z') + 1):
                res = dfs(current_s + chr(char_code))
                if res:
                    return res
            return None

        # Optimization: Iterative approach might be safer for stack depth
        # Or just use random generation if L is large.
        # Given L <= 8, DFS is fine.
        return dfs("")

def find_collision(B: int, M: int, L: int) -> tuple:
    solver = Solution()
    return solver.find_collision(B, M, L)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    B = int(input_data[0])
    M = int(input_data[1])
    L = int(input_data[2])
    
    s1, s2 = find_collision(B, M, L)
    print(s1)
    print(s2)

if __name__ == "__main__":
    main()
