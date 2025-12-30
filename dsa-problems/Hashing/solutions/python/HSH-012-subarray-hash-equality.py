import sys

# Increase recursion depth
sys.setrecursionlimit(2000)

class Solution:
    def check_subarray_equality(self, arr: list, queries: list) -> list:
        n = len(arr)
        MOD1 = 10**9 + 7
        BASE1 = 100003
        MOD2 = 10**9 + 9
        BASE2 = 100019
        
        h1 = [0] * (n + 1)
        p1 = [1] * (n + 1)
        h2 = [0] * (n + 1)
        p2 = [1] * (n + 1)
        
        for i in range(n):
            val = arr[i]
            
            h1[i+1] = (h1[i] * BASE1 + val) % MOD1
            p1[i+1] = (p1[i] * BASE1) % MOD1
            
            h2[i+1] = (h2[i] * BASE2 + val) % MOD2
            p2[i+1] = (p2[i] * BASE2) % MOD2
            
        def get_hash(h, p, l, r, mod):
            length = r - l + 1
            return (h[r+1] - h[l] * p[length]) % mod
            
        results = []
        for l1, r1, l2, r2 in queries:
            if r1 - l1 != r2 - l2:
                results.append(False)
                continue
                
            hash1_s1 = get_hash(h1, p1, l1, r1, MOD1)
            hash1_s2 = get_hash(h1, p1, l2, r2, MOD1)
            
            if hash1_s1 != hash1_s2:
                results.append(False)
                continue
                
            hash2_s1 = get_hash(h2, p2, l1, r1, MOD2)
            hash2_s2 = get_hash(h2, p2, l2, r2, MOD2)
            
            results.append(hash2_s1 == hash2_s2)
            
        return results

def check_subarray_equality(arr: list, queries: list) -> list:
    solver = Solution()
    return solver.check_subarray_equality(arr, queries)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        arr = []
        for _ in range(n):
            arr.append(int(next(iterator)))
            
        q = int(next(iterator))
        queries = []
        for _ in range(q):
            l1 = int(next(iterator))
            r1 = int(next(iterator))
            l2 = int(next(iterator))
            r2 = int(next(iterator))
            queries.append([l1, r1, l2, r2])
            
        result = check_subarray_equality(arr, queries)
        for ans in result:
            print("true" if ans else "false")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
