import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    r_count = int(input_data[ptr])
    ptr += 1
    nodes = {}
    for i in range(1, n + 1):
        val = int(input_data[ptr])
        ptr += 1
        nxt = int(input_data[ptr])
        ptr += 1
        nodes[i] = (val, nxt)
        
    roots = []
    for _ in range(r_count):
        roots.append(int(input_data[ptr]))
        ptr += 1
        
    reachable = set()
    stack = []
    
    for r in roots:
        if r != 0 and r not in reachable:
            reachable.add(r)
            stack.append(r)
            
    while stack:
        u = stack.pop()
        _, nxt = nodes[u]
        if nxt != 0 and nxt not in reachable:
            reachable.add(nxt)
            stack.append(nxt)
            
    k = len(reachable)
    print(k)
    sorted_ids = sorted(list(reachable))
    for nid in sorted_ids:
        print(f"{nid} {nodes[nid][0]}")


if __name__ == "__main__":
    solve()
