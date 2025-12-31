import sys

class Solution:
    def find_matrix(self, A: list, B: list) -> bool:
        n, m = len(A), len(A[0])
        p, q = len(B), len(B[0])
        
        if p > n or q > m:
            return False
            
        MOD = 10**9 + 7
        BASE1 = 313
        BASE2 = 317
        
        # Helper to compute hash of B
        def compute_target_hash():
            row_hashes = []
            for i in range(p):
                h = 0
                for j in range(q):
                    h = (h * BASE1 + B[i][j]) % MOD
                row_hashes.append(h)
            
            final_h = 0
            for h in row_hashes:
                final_h = (final_h * BASE2 + h) % MOD
            return final_h
            
        target_hash = compute_target_hash()
        
        # Precompute row hashes of A
        # row_hashes[i][j] is hash of A[i][j...j+q-1]
        row_hashes = [[0] * (m - q + 1) for _ in range(n)]
        power1 = pow(BASE1, q - 1, MOD)
        
        for i in range(n):
            h = 0
            for k in range(q):
                h = (h * BASE1 + A[i][k]) % MOD
            row_hashes[i][0] = h
            
            for j in range(1, m - q + 1):
                remove = (A[i][j - 1] * power1) % MOD
                h = (h - remove + MOD) % MOD
                h = (h * BASE1 + A[i][j + q - 1]) % MOD
                row_hashes[i][j] = h
                
        # Compute column hashes on row_hashes
        power2 = pow(BASE2, p - 1, MOD)
        
        for j in range(m - q + 1):
            h = 0
            for k in range(p):
                h = (h * BASE2 + row_hashes[k][j]) % MOD
            
            if h == target_hash:
                return True
                
            for i in range(1, n - p + 1):
                remove = (row_hashes[i - 1][j] * power2) % MOD
                h = (h - remove + MOD) % MOD
                h = (h * BASE2 + row_hashes[i + p - 1][j]) % MOD
                
                if h == target_hash:
                    return True
                    
        return False

def find_matrix(A: list, B: list) -> bool:
    solver = Solution()
    return solver.find_matrix(A, B)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        A = []
        for _ in range(n):
            row = []
            for _ in range(m):
                row.append(int(next(iterator)))
            A.append(row)
            
        p = int(next(iterator))
        q = int(next(iterator))
        B = []
        for _ in range(p):
            row = []
            for _ in range(q):
                row.append(int(next(iterator)))
            B.append(row)
            
        result = find_matrix(A, B)
        print("true" if result else "false")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
