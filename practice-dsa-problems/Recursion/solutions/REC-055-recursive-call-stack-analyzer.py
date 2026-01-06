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
    s_start = int(input_data[ptr])
    ptr += 1
    frames = []
    for _ in range(n):
        frames.append(int(input_data[ptr]))
        ptr += 1
        
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[ptr])
        ptr += 1
        v = int(input_data[ptr])
        ptr += 1
        tp = input_data[ptr]
        ptr += 1
        adj[u].append((v, tp == "T"))
        
    res_memo = {}

    def peak(u):
        if u in res_memo:
            return res_memo[u]
        
        # Max peak usage in this subtree/call-chain
        # Base: my frame size
        my_frame = frames[u - 1]
        best = my_frame
        
        for v, is_tail in adj[u]:
            p_v = peak(v)
            if is_tail:
                # Tail call: Reuses current frame or transition?
                # Usually TCO means we replace stack frame. 
                # So max usage is max(my_frame, child_peak).
                # (Child doesn't add on top of me).
                best = max(best, p_v)
            else:
                # Normal call: Child adds on top.
                # max usage = max(my_frame + p_v) (if p_v is relative peak?)
                # Wait, p_v is absolute peak of that chain.
                # So `my_frame + p_v`.
                best = max(best, my_frame + p_v)
                
        res_memo[u] = best
        return best

    sys.setrecursionlimit(300000)
    print(peak(s_start))


if __name__ == "__main__":
    solve()
