import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    lst = []
    for _ in range(n):
        lst.append(int(input_data[ptr]))
        ptr += 1
        
    k_tokens = int(input_data[ptr])
    ptr += 1
    
    tokens = {}
    for _ in range(k_tokens):
        tid = int(input_data[ptr])
        ptr += 1
        l = int(input_data[ptr])
        ptr += 1
        r = int(input_data[ptr])
        ptr += 1
        exp = int(input_data[ptr])
        ptr += 1
        tokens[tid] = (l, r, exp)
        
    q = int(input_data[ptr])
    ptr += 1
    
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        
        if op == 'GET':
            pos = int(input_data[ptr])
            ptr += 1
            t = int(input_data[ptr])
            ptr += 1
            if 1 <= pos <= len(lst):
                print(lst[pos - 1])
            else:
                print("-1")
        elif op == 'INS':
            tid = int(input_data[ptr])
            ptr += 1
            pos = int(input_data[ptr])
            ptr += 1
            x = int(input_data[ptr])
            ptr += 1
            t = int(input_data[ptr])
            ptr += 1
            if tid in tokens:
                l, r, exp = tokens[tid]
                if t <= exp and l <= pos <= r:
                    lst.insert(pos - 1, x)
        elif op == 'DEL':
            tid = int(input_data[ptr])
            ptr += 1
            pos = int(input_data[ptr])
            ptr += 1
            t = int(input_data[ptr])
            ptr += 1
            if tid in tokens:
                l, r, exp = tokens[tid]
                if t <= exp and l <= pos <= r:
                    if 1 <= pos <= len(lst):
                        lst.pop(pos - 1)
if __name__ == '__main__':
    solve()