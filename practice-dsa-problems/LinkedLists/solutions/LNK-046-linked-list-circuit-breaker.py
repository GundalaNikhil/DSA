import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    F = int(input_data[ptr])
    ptr += 1
    T = int(input_data[ptr])
    ptr += 1
    L_bound = int(input_data[ptr])
    ptr += 1
    U_bound = int(input_data[ptr])
    ptr += 1
    lst = []
    for _ in range(n):
        lst.append(int(input_data[ptr]))
        ptr += 1
        
    q = int(input_data[ptr])
    ptr += 1
    
    consecutive_failures = 0
    open_remaining = 0
    
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        
        if op == 'GET':
            pos = int(input_data[ptr])
            ptr += 1
            if 1 <= pos <= len(lst):
                print(lst[pos - 1])
            else:
                print("-1")
        else:
            # Operation that might trigger circuit breaker
            if open_remaining > 0:
                if op == 'INS':
                    ptr += 2
                else:
                    ptr += 1
                open_remaining -= 1
                continue
                
            success = False
            if op == 'INS':
                pos = int(input_data[ptr])
                ptr += 1
                x = int(input_data[ptr])
                ptr += 1
                if L_bound <= x <= U_bound:
                    lst.insert(pos - 1, x)
                    success = True
            elif op == 'DEL':
                pos = int(input_data[ptr])
                ptr += 1
                if 1 <= pos <= len(lst):
                    lst.pop(pos - 1)
                    success = True
                    
            if success:
                consecutive_failures = 0
            else:
                consecutive_failures += 1
                if consecutive_failures >= F:
                    open_remaining = T
                    consecutive_failures = 0
if __name__ == '__main__':
    solve()