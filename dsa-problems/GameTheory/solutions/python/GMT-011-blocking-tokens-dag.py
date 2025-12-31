from typing import List
import sys

# Increase recursion depth just in case
sys.setrecursionlimit(20000)

def blocking_tokens(n: int, edges: List[List[int]], u: int, v: int) -> str:
    adj = [[] for _ in range(n + 1)]
    for a, b in edges:
        adj[a].append(b)
    
    # memo[u][v] stores result: None=unknown, False=Losing, True=Winning
    memo = {}

    def can_win(curr_u, curr_v):
        state = (curr_u, curr_v)
        if state in memo:
            return memo[state]
        
        # Try moving u
        for next_u in adj[curr_u]:
            if next_u == curr_v: continue
            if not can_win(next_u, curr_v):
                memo[state] = True
                return True
        
        # Try moving v
        for next_v in adj[curr_v]:
            if next_v == curr_u: continue
            if not can_win(curr_u, next_v):
                memo[state] = True
                return True
                
        memo[state] = False
        return False

    return "First" if can_win(u, v) else "Second"

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
            u_edge = int(next(iterator))
            v_edge = int(next(iterator))
            edges.append([u_edge, v_edge])
        u = int(next(iterator))
        v = int(next(iterator))
            
        print(blocking_tokens(n, edges, u, v))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
