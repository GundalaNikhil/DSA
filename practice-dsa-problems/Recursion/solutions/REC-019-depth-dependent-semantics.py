import sys
sys.setrecursionlimit(300000)
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    nodes = {}
    for i in range(1, n + 1):
        t = int(input_data[ptr])
        ptr += 1
        v_str = input_data[ptr]
        ptr += 1
        l = int(input_data[ptr])
        ptr += 1
        r = int(input_data[ptr])
        ptr += 1
        nodes[i] = (t, v_str, l, r)
        
    def evaluate(u, depth):
        # Base case t=0 assumed leaf
        t, v_str, l, r = nodes[u]
        
        if t == 0:
             # Leaf node has value in v_str?
             # Or leaf takes v_str as number.
            return int(v_str)
            
        left_val = evaluate(l, depth + 1)
        right_val = evaluate(r, depth + 1)
        
        if depth % 2 == 0:
            if v_str == '+':
                return max(left_val, right_val) # Weird semantic? + means max?
            else:
                return min(left_val, right_val)
        else:
            if v_str == '+':
                return min(left_val, right_val)
            else:
                return max(left_val, right_val)

    if n > 0:
        print(evaluate(1, 0))
    else:
        print(0)
if __name__ == '__main__':
    solve()