import sys

# Increase recursion depth just in case, though not needed for this iterative solution
sys.setrecursionlimit(200000)

class Solution:
    def lcp_queries(self, s: str, queries: list[tuple[int, int]]) -> list[int]:
        n = len(s)
        if n == 0:
            return [0] * len(queries)
            
        # 1. Build SA
        sa = list(range(n))
        rank = [ord(c) for c in s]
        new_rank = [0] * n
        
        k = 1
        while k < n:
            key_func = lambda i: (rank[i], rank[i + k] if i + k < n else -1)
            sa.sort(key=key_func)
            
            new_rank[sa[0]] = 0
            for i in range(1, n):
                prev = sa[i-1]
                curr = sa[i]
                if key_func(prev) == key_func(curr):
                    new_rank[curr] = new_rank[prev]
                else:
                    new_rank[curr] = new_rank[prev] + 1
            
            rank = list(new_rank)
            if rank[sa[n-1]] == n - 1:
                break
            k *= 2
            
        # 2. Build LCP
        lcp = [0] * (n - 1)
        k_val = 0
        for i in range(n):
            if rank[i] == n - 1:
                k_val = 0
                continue
            j = sa[rank[i] + 1]
            while i + k_val < n and j + k_val < n and s[i + k_val] == s[j + k_val]:
                k_val += 1
            lcp[rank[i]] = k_val
            if k_val > 0:
                k_val -= 1
                
        # 3. Build Sparse Table
        m = len(lcp)
        if m == 0:
            return [n - q[0] if q[0] == q[1] else 0 for q in queries]
            
        logs = [0] * (m + 1)
        for i in range(2, m + 1):
            logs[i] = logs[i // 2] + 1
            
        K = logs[m]
        st = [[0] * m for _ in range(K + 1)]
        for i in range(m):
            st[0][i] = lcp[i]
            
        for k in range(1, K + 1):
            for i in range(m - (1 << k) + 1):
                st[k][i] = min(st[k - 1][i], st[k - 1][i + (1 << (k - 1))])
                
        def query(L, R):
            if L > R: return 0
            j = logs[R - L + 1]
            return min(st[j][L], st[j][R - (1 << j) + 1])
            
        ans = []
        for i, j in queries:
            if i == j:
                ans.append(n - i)
            else:
                r1 = rank[i]
                r2 = rank[j]
                if r1 > r2:
                    r1, r2 = r2, r1
                ans.append(query(r1, r2 - 1))
        return ans

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    q = int(input_data[1])
    queries = []
    idx = 2
    for _ in range(q):
        i = int(input_data[idx])
        j = int(input_data[idx + 1])
        queries.append((i, j))
        idx += 2
        
    sol = Solution()
    ans = sol.lcp_queries(s, queries)
    sys.stdout.write("\n".join(str(x) for x in ans) + "\n")

if __name__ == "__main__":
    main()