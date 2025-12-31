from typing import List

def kayles_on_graph(n: int, edges: List[List[int]]) -> str:
    adj_mask = [0] * n
    for u, v in edges:
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
        
    memo = {}

    def can_win(mask):
        if mask == 0:
            return False
        if mask in memo:
            return memo[mask]
        
        for u in range(n):
            if (mask >> u) & 1:
                remove_mask = (1 << u) | adj_mask[u]
                next_mask = mask & ~remove_mask
                if not can_win(next_mask):
                    memo[mask] = True
                    return True
        
        memo[mask] = False
        return False

    return "First" if can_win((1 << n) - 1) else "Second"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append([u, v])
            
        print(kayles_on_graph(n, edges))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
