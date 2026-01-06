import sys


def dominates(a, b):
    strict = False
    for i in range(len(a)):
        if a[i] < b[i]:
            return False
        if a[i] > b[i]:
            strict = True
            return strict


def concurrent(a, b):
    return not dominates(a, b) and not dominates(b, a) and a != b


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    q = int(input_data[ptr])
    ptr += 1
    d = int(input_data[ptr])
    ptr += 1
    
    pos_clocks = {}
    
    for _ in range(q):
        pos = int(input_data[ptr])
        ptr += 1
        clock = []
        for _ in range(d):
            clock.append(int(input_data[ptr]))
            ptr += 1
            
        if pos not in pos_clocks:
            pos_clocks[pos] = []
        pos_clocks[pos].append(tuple(clock))
        
        total_concurrent = 0
        all_clocks = []
        for p_list in pos_clocks.values():
            all_clocks.extend(p_list)
            
        n_clocks = len(all_clocks)
        for i in range(n_clocks):
            for j in range(i + 1, n_clocks):
                if concurrent(all_clocks[i], all_clocks[j]):
                    total_concurrent += 1
                    
        print(total_concurrent)


if __name__ == "__main__":
    solve()
