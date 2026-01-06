import sys
from collections import deque


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    r_count = int(input_data[ptr])
    ptr += 1
    l_limit = int(input_data[ptr])
    ptr += 1
    roots = []
    for _ in range(r_count):
        roots.append(int(input_data[ptr]))
        ptr += 1
        
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[ptr])
        ptr += 1
        v = int(input_data[ptr])
        ptr += 1
        adj[u].append(v)
        
    marked = [False] * (n + 1)
    recursive_count = 0
    iterative_count = 0
    queue = deque()

    def dfs_recursive(u, depth):
        nonlocal recursive_count
        if marked[u]:
            return
        marked[u] = True
        recursive_count += 1
        
        if depth >= l_limit:
            # Switch to iterative if depth limit hit (simulating stack overflow prevention?)
            # Add boundary nodes to queue for iterative processing?
            for v in adj[u]:
                if not marked[v]:
                    queue.append(v)
            return

        for v in adj[u]:
            dfs_recursive(v, depth + 1)

    sys.setrecursionlimit(300000)
    
    # Phase 1: Recursive from roots up to depth limit
    for r in roots:
        dfs_recursive(r, 0)
        
    # Phase 2: Iterative for remaining
    while queue:
        u = queue.popleft()
        if marked[u]:
            continue
            
        # Standard iterative DFS/BFS from here? 
        # Code used a stack `stack = [u]` inside `while queue`.
        stack = [u]
        while stack:
            curr = stack.pop()
            if not marked[curr]: # Logic check: u might be marked by earlier queue proc
                marked[curr] = True
                iterative_count += 1
                
            # Wait, `curr` is popped. If already marked, skip children?
            # Or is this graph traversal where updated `marked` prevents loops?
            # Correct iterative DFS:
            # if marked[curr]: continue; marked[curr]=True....
            # But `u` from queue was not marked (checked before push).
            # The issue is `stack` pushes children.
            
            for v in adj[curr]:
                if not marked[v]:
                    # Push to stack to visit
                    # To avoid duplicates in stack, usually we mark on push or handle on pop.
                    # Let's handle on pop.
                    visited_check = False # Simulating logic
                    stack.append(v)
                    # But in typical DFS, we might want to mark instantly to avoid re-pushing?
                    # Let's stick to standard: Mark on pop (or check on pop).
                    
    # Re-evaluating the iterative count logic from original:
    # `iterative_count += 1` inside stack loop.
    # It counts nodes visited iteratively.
    
    # Fix: Count *unique* nodes visited in iterative phase?
    # `marked` array handles uniqueness globally.
    
    # Correct Iterative DFS (handling uniqueness):
    # Queue contains start nodes for iterative phase.
    
    iterative_stack = []
    # Move queue items to stack
    while queue:
        iterative_stack.append(queue.popleft())
        
    while iterative_stack:
        u = iterative_stack.pop()
        if marked[u]:
            continue
        marked[u] = True
        iterative_count += 1
        for v in adj[u]:
            if not marked[v]:
                iterative_stack.append(v)

    print(f"{recursive_count} {iterative_count}")


if __name__ == "__main__":
    sys.setrecursionlimit(300000)
    solve()
