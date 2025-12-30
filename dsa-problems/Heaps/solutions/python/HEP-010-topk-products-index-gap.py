import sys
import heapq

class Solution:
    def top_k_products(self, A: list, B: list, k: int, d: int) -> list:
        n = len(A)
        m = len(B)
        
        # Max heap: stores (-val, r, c, dir)
        pq = []
        visited = set()
        
        def push(r, c, direction):
            if 0 <= r < n and 0 <= c < m and abs(r - c) >= d:
                key = (r, c)
                if key not in visited:
                    visited.add(key)
                    val = A[r] * B[c]
                    heapq.heappush(pq, (-val, r, c, direction))

        # TL Starts
        if d < n: push(d, 0, 1)
        if d < m and d > 0: push(0, d, 1)
        elif d == 0: push(0, 0, 1)
        
        # BR Starts
        if d < n:
            start_i = n - 1
            start_j = min(m - 1, n - 1 - d)
            if start_j >= 0: push(start_i, start_j, -1)
            
        if d < m and d > 0:
            start_j = m - 1
            start_i = min(n - 1, m - 1 - d)
            if start_i >= 0: push(start_i, start_j, -1)
            
        res = []
        while k > 0 and pq:
            val, r, c, direction = heapq.heappop(pq)
            res.append(-val)
            k -= 1
            
            if direction == 1:
                push(r + 1, c, 1)
                push(r, c + 1, 1)
            else:
                push(r - 1, c, -1)
                push(r, c - 1, -1)
                
        return res

def top_k_products(A: list, B: list, k: int, d: int) -> list:
    solver = Solution()
    return solver.top_k_products(A, B, k, d)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        m = int(next(it))
        k = int(next(it))
        d = int(next(it))
        A = []
        for _ in range(n):
            A.append(int(next(it)))
        B = []
        for _ in range(m):
            B.append(int(next(it)))
            
        result = top_k_products(A, B, k, d)
        print(" ".join(map(str, result)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
