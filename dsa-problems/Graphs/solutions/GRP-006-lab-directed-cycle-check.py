from typing import List

def has_cycle(n: int, adj: List[List[int]]) -> bool:
    visited = [False] * n
    rec_stack = [False] * n
    
    def dfs(node):
        visited[node] = True
        rec_stack[node] = True
        
        for neighbor in adj[node]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif rec_stack[neighbor]:
                return True  # Back edge - cycle detected
        
        rec_stack[node] = False
        return False
    
    for i in range(n):
        if not visited[i]:
            if dfs(i):
                return True
    
    return False


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
