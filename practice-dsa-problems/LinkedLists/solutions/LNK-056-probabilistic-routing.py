import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    jumps = []
    for _ in range(n):
        jumps.append(int(input_data[ptr]))
        ptr += 1
        
    probs = []
    for _ in range(n):
        probs.append(int(input_data[ptr]))
        ptr += 1
        
    e = [0.0] * (n + 2)
    for i in range(n, 0, -1):
        p = probs[i - 1] / 1000.0
        j = jumps[i - 1]
        if j == 0:
            e[i] = 1.0 + e[i + 1]
        else:
            e[i] = 1.0 + p * e[j] + (1 - p) * e[i + 1]
            
    print(int(round(e[1] * 1000)))


if __name__ == "__main__":
    solve()
