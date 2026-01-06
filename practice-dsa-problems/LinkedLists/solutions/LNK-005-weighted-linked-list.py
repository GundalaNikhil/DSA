import sys
from bisect import bisect_right


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    values = []
    for _ in range(n):
        values.append(int(input_data[ptr]))
        ptr += 1
        
    weights = []
    for _ in range(n):
        weights.append(int(input_data[ptr]))
        ptr += 1
        
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + weights[i]
        
    q = int(input_data[ptr])
    ptr += 1
    
    out = []
    for _ in range(q):
        b = int(input_data[ptr])
        ptr += 1
        idx = bisect_right(pref, b) - 1
        if idx == 0:
            out.append("-1")
        else:
            out.append(str(values[idx - 1]))
            
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    solve()
