import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    R = int(input_data[ptr])
    ptr += 1
    B = int(input_data[ptr])
    ptr += 1
    replicas = []
    for _ in range(R):
        replicas.append([int(input_data[ptr + j]) for j in range(n)])
        ptr += n
        
    res = []
    threshold = R - B
    
    for i in range(n):
        counts = {}
        for r in range(R):
            v = replicas[r][i]
            counts[v] = counts.get(v, 0) + 1
            
        candidates = [v for v, c in counts.items() if c >= threshold]
        
        if candidates:
            res.append(str(min(candidates)))
        else:
            res.append("*")
            
    print(*(res))


if __name__ == "__main__":
    solve()
