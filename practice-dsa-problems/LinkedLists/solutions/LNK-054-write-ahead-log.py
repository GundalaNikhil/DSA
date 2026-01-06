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
        
    q = int(input_data[ptr])
    ptr += 1
    
    for _ in range(q):
        commit = int(input_data[ptr])
        ptr += 1
        tp = input_data[ptr]
        ptr += 1
        pos = int(input_data[ptr])
        ptr += 1
        
        if tp == "INS":
            x = int(input_data[ptr])
            ptr += 1
            if commit:
                if 1 <= pos <= len(lst) + 1:
                    lst.insert(pos - 1, x)
        elif tp == "DEL":
            if commit:
                if 1 <= pos <= len(lst):
                    lst.pop(pos - 1)
        elif tp == "SET":
            x = int(input_data[ptr])
            ptr += 1
            if commit:
                if 1 <= pos <= len(lst):
                    lst[pos - 1] = x
                    
        print(*(lst))


if __name__ == "__main__":
    solve()
