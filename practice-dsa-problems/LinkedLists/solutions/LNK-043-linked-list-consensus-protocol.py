import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    R = int(input_data[ptr])
    ptr += 1
    M = int(input_data[ptr])
    ptr += 1
    t = int(input_data[ptr])
    ptr += 1
    results = []
    for _ in range(t):
        p = int(input_data[ptr])
        ptr += 1
        
        counts = {}
        for _ in range(p):
            rid = int(input_data[ptr])
            ptr += 1
            val = int(input_data[ptr])
            ptr += 1
            counts[val] = counts.get(val, 0) + 1
            
        committed = -1
        leaders = [v for v, c in counts.items() if c >= M]
        if leaders:
            committed = min(leaders)
        results.append(str(committed))
        
    print("\n".join(results))


if __name__ == "__main__":
    solve()
