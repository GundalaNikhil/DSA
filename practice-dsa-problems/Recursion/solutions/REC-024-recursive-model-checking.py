import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    k_limit = int(input_data[ptr])
    ptr += 1
    s_start = int(input_data[ptr])
    ptr += 1
    nodes = []
    for _ in range(n):
        t = input_data[ptr]
        ptr += 1
        v = int(input_data[ptr])
        ptr += 1
        nodes.append((t, v))
        
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[ptr])
        ptr += 1
        v = int(input_data[ptr])
        ptr += 1
        adj[u].append(v)
        
    curr_dp = [0] * (n + 1)
    
    # Initialize Terminal states
    for i in range(1, n + 1):
        t, v = nodes[i - 1]
        if t == "T":
            curr_dp[i] = v
        else:
            curr_dp[i] = 0
            
    # Fixpoint iteration up to k_limit
    for k in range(1, k_limit + 1):
        next_dp = [0] * (n + 1)
        for i in range(1, n + 1):
            t, v = nodes[i - 1]
            if t == "T":
                next_dp[i] = v
            elif t == "A": # All paths must be valid (1)
                if not adj[i]:
                     next_dp[i] = 0 # No paths = false? Or Vacuously true? Assuming false if "All paths" need to reach.
                else:
                    all_ok = 1
                    for v_succ in adj[i]:
                        if curr_dp[v_succ] == 0:
                            all_ok = 0
                            break
                    next_dp[i] = all_ok
            elif t == "E": # Exists path
                any_ok = 0
                for v_succ in adj[i]:
                    if curr_dp[v_succ] == 1:
                        any_ok = 1
                        break
                next_dp[i] = any_ok
                
        curr_dp = next_dp
        
    print(curr_dp[s_start])
if __name__ == "__main__":
    solve()