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
    s = int(input_data[ptr])
    ptr += 1
    t = int(input_data[ptr])
    ptr += 1
    l1 = int(input_data[ptr])
    ptr += 1
    l2 = int(input_data[ptr])
    ptr += 1
    adj = [[] for _ in range(n + 1)]
    rev_adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[ptr])
        ptr += 1
        v = int(input_data[ptr])
        ptr += 1
        adj[u].append(v)
        rev_adj[v].append(u)
        
    # BFS from s (forward)
    dist_s = {s: 0}
    queue_s = deque([s])
    
    while queue_s:
        u = queue_s.popleft()
        d = dist_s[u]
        
        if d < l1:
            for v in adj[u]:
                if v not in dist_s:
                    dist_s[v] = d + 1
                    queue_s.append(v)
                    
    # BFS from t (backward, on rev graph)
    dist_t = {t: 0}
    queue_t = deque([t])
    
    while queue_t:
        u = queue_t.popleft()
        d = dist_t[u]
        
        if d < l2:
            for v in rev_adj[u]:
                if v not in dist_t:
                    dist_t[v] = d + 1
                    queue_t.append(v)
                    
    # Find meet point
    min_dist = float("inf")
    
    for u in dist_s:
        if u in dist_t:
            min_dist = min(min_dist, dist_s[u] + dist_t[u])
            
    if min_dist == float("inf"):
        print("-1")
    else:
        print(min_dist)


if __name__ == "__main__":
    solve()
