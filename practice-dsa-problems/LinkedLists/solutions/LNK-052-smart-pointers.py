import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    strong_counts = {}
    for i in range(1, n + 1):
        strong_counts[i] = int(input_data[ptr])
        ptr += 1
        
    m_links = int(input_data[ptr])
    ptr += 1
    
    links = {i: set() for i in range(1, n + 1)}
    for _ in range(m_links):
        u = int(input_data[ptr])
        ptr += 1
        v = int(input_data[ptr])
        ptr += 1
        links[u].add(v)
        
    q = int(input_data[ptr])
    ptr += 1
    
    alive = [True] * (n + 1)
    target_counts = {i: 0 for i in range(1, n + 1)}
    
    # Initialize target counts
    for u in range(1, n + 1):
        for v in links[u]:
            target_counts[v] += 1
            
    def destroy(u):
        if not alive[u]:
            return
        alive[u] = False
        for v in links[u]:
            target_counts[v] -= 1
            if strong_counts[v] + target_counts[v] <= 0:
                destroy(v)
        links[u] = set()

    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        
        if op == "INC":
            u = int(input_data[ptr])
            ptr += 1
            if alive[u]:
                strong_counts[u] += 1
        elif op == "DEC":
            u = int(input_data[ptr])
            ptr += 1
            if alive[u]:
                strong_counts[u] = max(0, strong_counts[u] - 1)
                if strong_counts[u] + target_counts[u] <= 0:
                    destroy(u)
        elif op == "LINK":
            u = int(input_data[ptr])
            ptr += 1
            v = int(input_data[ptr])
            ptr += 1
            if alive[u] and alive[v] and v not in links[u]:
                links[u].add(v)
                target_counts[v] += 1
        elif op == "UNLINK":
            u = int(input_data[ptr])
            ptr += 1
            v = int(input_data[ptr])
            ptr += 1
            if alive[u] and alive[v] and v in links[u]:
                links[u].remove(v)
                target_counts[v] -= 1
                if strong_counts[v] + target_counts[v] <= 0:
                    destroy(v)
                    
    for i in range(1, n + 1):
        if (alive[i] and strong_counts[i] + target_counts[i] <= 0):
                destroy(i)
                
    res = [i for i in range(1, n + 1) if alive[i]]
    print(len(res))
    print(*(res))


if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    solve()
