import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

class Solution:
    def process_operations(self, s: str, operations: list) -> list:
        n = len(s)
        MOD = 10**9 + 7
        BASE = 313
        
        chars = list(s)
        tree = [0] * (4 * n)
        power = [1] * (n + 1)
        
        for i in range(1, n + 1):
            power[i] = (power[i - 1] * BASE) % MOD
            
        def build(node, start, end):
            if start == end:
                tree[node] = ord(chars[start])
                return
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            
            right_len = end - mid
            tree[node] = (tree[2 * node] * power[right_len] + tree[2 * node + 1]) % MOD
            
        def update(node, start, end, idx, val):
            if start == end:
                chars[idx] = val
                tree[node] = ord(val)
                return
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node, start, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, end, idx, val)
                
            right_len = end - mid
            tree[node] = (tree[2 * node] * power[right_len] + tree[2 * node + 1]) % MOD
            
        def query(node, start, end, l, r):
            if r < start or end < l:
                return -1
            if l <= start and end <= r:
                return tree[node]
            
            mid = (start + end) // 2
            p1 = query(2 * node, start, mid, l, r)
            p2 = query(2 * node + 1, mid + 1, end, l, r)
            
            if p1 == -1: return p2
            if p2 == -1: return p1
            
            right_start = max(mid + 1, l)
            right_end = min(end, r)
            right_len = right_end - right_start + 1
            
            return (p1 * power[right_len] + p2) % MOD
            
        build(1, 0, n - 1)
        results = []
        
        for op in operations:
            if op[0] == 'U':
                idx = int(op[1])
                c = op[2]
                update(1, 0, n - 1, idx, c)
            else:
                l = int(op[1])
                r = int(op[2])
                results.append(query(1, 0, n - 1, l, r))
                
        return results

def process_operations(s: str, operations: list) -> list:
    solver = Solution()
    return solver.process_operations(s, operations)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        s = next(iterator)
        q = int(next(iterator))
        operations = []
        for _ in range(q):
            type_op = next(iterator)
            if type_op == 'U':
                idx = next(iterator)
                c = next(iterator)
                operations.append(['U', idx, c])
            else:
                l = next(iterator)
                r = next(iterator)
                operations.append(['Q', l, r])
                
        result = process_operations(s, operations)
        for val in result:
            print(val)
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
