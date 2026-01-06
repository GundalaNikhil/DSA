import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    nodes = []
    all_descriptions = []
    for _ in range(n):
        tp = input_data[ptr]
        ptr += 1
        if tp in ('INT', 'BOOL'):
            val = input_data[ptr]
            ptr += 1
            all_descriptions.append((tp, val))
        else:
            c1 = int(input_data[ptr])
            ptr += 1
            c2 = int(input_data[ptr])
            ptr += 1
            all_descriptions.append((tp, c1, c2))
            
    # Find root
    parents = [0] * (n + 1)
    for i, desc in enumerate(all_descriptions): # 0-indexed list, node ID i+1
        node_id = i + 1
        if len(desc) == 3:
            parents[desc[1]] = 1
            parents[desc[2]] = 1
            
    root = -1
    for i in range(1, n + 1):
        if parents[i] == 0:
            root = i
            break
            
    memo = {}

    def get_type(u):
        if u in memo:
            return memo[u]
            
        desc = all_descriptions[u - 1]
        tp = desc[0]
        
        if tp == 'INT':
            res = 'INT'
        elif tp == 'BOOL':
            res = 'BOOL'
        elif tp in ('ADD', 'AND', 'EQ'):
            t1 = get_type(desc[1])
            t2 = get_type(desc[2])
            
            if t1 == 'TYPE_ERROR' or t2 == 'TYPE_ERROR':
                res = 'TYPE_ERROR'
            elif tp == 'ADD':
                if t1 == 'INT' and t2 == 'INT':
                    res = 'INT'
                else:
                    res = 'TYPE_ERROR'
            elif tp == 'AND':
                if t1 == 'BOOL' and t2 == 'BOOL':
                    res = 'BOOL'
                else:
                    res = 'TYPE_ERROR'
            elif tp == 'EQ':
                 # EQ check: usually same types? Or any comparable?
                 # Python `t1 == t2` checks if types match (e.g. INT==INT).
                 # Assuming logic is: must compare same types.
                if t1 == t2:
                    res = 'BOOL'
                else:
                    res = 'TYPE_ERROR'
        else:
            res = 'TYPE_ERROR'
            
        memo[u] = res
        return res

    sys.setrecursionlimit(300000)
    print(get_type(root))
if __name__ == '__main__':
    solve()