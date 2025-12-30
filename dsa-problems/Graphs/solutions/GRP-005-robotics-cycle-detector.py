from typing import List

def has_cycle(n: int, adj: List[List[int]]) -> bool:
    visited = [False] * n
    
    def dfs(node, parent):
        visited[node] = True
        
        for neighbor in adj[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True  # Cycle detected
        
        return False
    
    for i in range(n):
        if not visited[i]:
            if dfs(i, -1):
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
