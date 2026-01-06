import sys
from collections import defaultdict

sys.setrecursionlimit(500000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    node_data = []
    adj = defaultdict(list)
    root = -1
    for i in range(1, n + 1):
        v = int(input_data[ptr])
        ptr += 1
        p = int(input_data[ptr])
        ptr += 1
        par = int(input_data[ptr])
        ptr += 1
        node_data.append((v, p))
        if par == 0:
            root = i
        else:
            adj[par].append(i)
            
    def evaluate(u, inherited):
        v, p = node_data[u - 1]
        effective = max(inherited, p)
        total = v * effective
        
        for v_child in adj[u]:
            total += evaluate(v_child, inherited) # Inherited or effective?
            # Problem name "Recursive Priority Inheritance" implies children inherit max from ancestors.
            # Original code said: total += evaluate(v_child, effective)
            # So let's stick to passing effective down.
            pass
            
        # Re-implement loop correctly without "pass" placeholder messing up logic
        for v_child in adj[u]:
            total += evaluate(v_child, effective)
            
        return total

    if root != -1:
        print(evaluate(root, 0))
    else:
        print(0)


if __name__ == "__main__":
    solve()
