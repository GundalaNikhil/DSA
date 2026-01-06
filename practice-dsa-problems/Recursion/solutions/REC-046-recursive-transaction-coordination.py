import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    nodes = []
    adj = [[] for _ in range(n + 1)]
    root = -1
    for i in range(1, n + 1):
        d = int(input_data[ptr])
        ptr += 1
        l = int(input_data[ptr])
        ptr += 1
        r = int(input_data[ptr])
        ptr += 1
        p = int(input_data[ptr])
        ptr += 1
        nodes.append((d, l, r))
        if p == 0:
            root = i
        else:
            adj[p].append(i)
            
    current_balance = 0
    sys.setrecursionlimit(300000)

    def evaluate(u):
        nonlocal current_balance
        start_balance = current_balance
        
        # Pre-order check? Or Post?
        # Logic: 
        # 1. Update from Children? No, current code calls evaluate(child) first.
        # "Transaction Coordination" with rollback often implies checking constraints after operations.
        # Original:
        # for child: evaluate(child)
        # then check self constraints?
        
        for v_child in adj[u]:
            evaluate(v_child)
            
        d_u, l_u, r_u = nodes[u - 1]
        potential_balance = current_balance + d_u
        
        if l_u <= potential_balance <= r_u:
            current_balance = potential_balance
        else:
            # Rollback to start of this subtree processing?
            # "Transaction Coordination"
            current_balance = start_balance


    if root != -1:
        evaluate(root)
        print(current_balance)
    else:
        print(0)


if __name__ == "__main__":
    solve()
