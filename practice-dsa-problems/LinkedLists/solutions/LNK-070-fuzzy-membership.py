import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    probs = []
    for _ in range(n):
        probs.append(int(input_data[ptr]))
        ptr += 1
        
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + probs[i]
        
    q = int(input_data[ptr])
    ptr += 1
    
    for _ in range(q):
        k = int(input_data[ptr])
        ptr += 1
        if 1 <= k <= n:
            print(pref[k])
        else:
            print(0)


if __name__ == "__main__":
    solve()
