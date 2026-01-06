import sys

sys.setrecursionlimit(300000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    h_max = int(input_data[ptr])
    ptr += 1
    adj = [[] for _ in range(n + 1)]
    values = [0] * (n + 1)
    root = -1
    for i in range(1, n + 1):
        v = int(input_data[ptr])
        ptr += 1
        p = int(input_data[ptr])
        ptr += 1
        values[i] = v
        if p == 0:
            root = i
        else:
            adj[p].append(i)
            
    ks = []
    for _ in range(h_max + 1):
        ks.append(int(input_data[ptr]))
        ptr += 1
        
    depth_sums = [0] * (h_max + 2) # h_max depth covered
    stack = [(root, 0)]
    
    while stack:
        u, d = stack.pop()
        if d <= h_max:
            depth_sums[d] += values[u]
            for v in adj[u]:
                stack.append((v, d + 1))
                
    for d in range(h_max + 1):
        if ks[d] != 0 and depth_sums[d] % ks[d] != 0:
             print("NO")
             return
             
    print("YES")


if __name__ == "__main__":
    solve()
