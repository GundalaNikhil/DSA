from typing import List
import sys

# Increase recursion depth for deep DAGs
sys.setrecursionlimit(200005)

def determine_winning_nodes(n: int, edges: List[List[int]]) -> List[str]:
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
    
    memo = {}

    def dfs(u):
        if u in memo:
            return memo[u]
        
        # Default is Losing (if no moves)
        is_winning = False
        for v in adj[u]:
            # If any neighbor is Losing, then u is Winning
            if not dfs(v):
                is_winning = True
                break
        
        memo[u] = is_winning
        return is_winning

    result = []
    for i in range(n):
        if dfs(i):
            result.append("Winning")
        else:
            result.append("Losing")
    return result

def main():
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
            
        result = determine_winning_nodes(n, edges)
        print(" ".join(result))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
