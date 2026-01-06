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
        tp = input_data[ptr]
        ptr += 1
        val = int(input_data[ptr])
        ptr += 1
        p = int(input_data[ptr])
        ptr += 1
        nodes.append((tp, val))
        if p == 0:
            root = i
        else:
            adj[p].append(i)
            
    memo = {}

    def find_strategy(u):
        if u in memo:
            return memo[u]
            
        tp, val = nodes[u - 1]
        
        if tp == 'L': # Leaf? Logic node?
            # Assuming L: Leaf/Literal. 1=True?
            res = (val == 1, [])
            memo[u] = res
            return res
            
        if tp == 'A': # AND node / All?
            # Need ONE child to win (weird for "A", maybe "Any"/"OR"?)
            # Or "Action"?
            # Logic: `curr_seq = [i + 1] + seq`. Sequence of choices?
            # `if is_win`: pick best sequence (lexicographically smallest?)
            # This looks like "OR" logic where we pick one branch.
            
            best_seq = None
            found_win = False
            
            for i, v_child in enumerate(adj[u]):
                is_win, seq = find_strategy(v_child)
                if is_win:
                    curr_seq = [i + 1] + seq # 1-based index of child choice locally?
                    if not found_win or curr_seq < best_seq:
                        best_seq = curr_seq
                        found_win = True
                        
            res = (found_win, best_seq if found_win else [])
            memo[u] = res
            return res
            
        else: # Assuming 'E' / 'Exists' / or 'All'?
            # Logic: `all_win = True`. Checks all children.
            # If all win, combine sequences? taking MAX sequence?
            
            all_seqs = []
            all_win = True
            
            for v_child in adj[u]:
                is_win, seq = find_strategy(v_child)
                if not is_win:
                    all_win = False
                    break
                all_seqs.append(seq)
                
            if all_win:
                if not all_seqs:
                    res = (True, [])
                else:
                    res = (True, max(all_seqs)) # Max sequence? Worst case path?
            else:
                res = (False, [])
                
            memo[u] = res
            return res

    sys.setrecursionlimit(300000)
    if root != -1:
        is_win, strategy = find_strategy(root)
        if is_win:
            print("WIN")
            print(*(strategy))
        else:
            print("LOSE")
    else:
        print("LOSE")
if __name__ == '__main__':
    solve()