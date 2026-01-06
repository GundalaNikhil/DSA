import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    vals = []
    caps = []
    adj = [[] for _ in range(n + 1)]
    root = -1
    for i in range(1, n + 1):
        v = int(input_data[ptr])
        ptr += 1
        cap = int(input_data[ptr])
        ptr += 1
        p = int(input_data[ptr])
        ptr += 1
        vals.append(v)
        caps.append(cap)
        if p == 0:
            root = i
        else:
            adj[p].append(i)
            
    for i in range(1, n + 1):
        adj[i].sort()
        
    def evaluate(u):
        v_u = vals[u - 1]
        cap_u = caps[u - 1]
        
        # Exception simulation
        if v_u < 0:
            return (0, True) # Throws exception
            
        total_sum = v_u
        failed_children = 0
        
        for v_child in adj[u]:
            child_sum, child_thrown = evaluate(v_child)
            if child_thrown:
                failed_children += 1
            else:
                total_sum += child_sum
                
        if failed_children > cap_u:
            return (0, True) # Propagate exception
            
        return (total_sum, False)

    if root != -1:
        sys.setrecursionlimit(300000)
        res_sum, res_thrown = evaluate(root)
        if res_thrown:
            print("EXCEPTION")
        else:
            print(res_sum)
    else:
        print(0)


if __name__ == "__main__":
    solve()
