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
        
    watches = {i: [] for i in range(1, n + 1 + 200000)}
    q = int(input_data[ptr])
    ptr += 1
    
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        
        if op == 'WATCH':
            wid = int(input_data[ptr])
            ptr += 1
            pos = int(input_data[ptr])
            ptr += 1
            watches[pos].append(wid)
        elif op == 'SET':
            pos = int(input_data[ptr])
            ptr += 1
            x = int(input_data[ptr])
            ptr += 1
            if 1 <= pos <= len(lst):
                lst[pos - 1] = x
                if watches[pos]:
                    triggered = sorted(watches[pos])
                    print(*(triggered))
                    watches[pos] = []
                else:
                    print(0)
        elif op == 'GET':
            pos = int(input_data[ptr])
            ptr += 1
            if 1 <= pos <= len(lst):
                print(lst[pos - 1])
            else:
                print("-1")
if __name__ == '__main__':
    solve()