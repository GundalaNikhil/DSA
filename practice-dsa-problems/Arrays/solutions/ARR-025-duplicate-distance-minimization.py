import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))
    except StopIteration:
        return
        
    
    last_seen = {}
    min_dist = float("inf")
    
    for i, x in enumerate(a):
        if x in last_seen:
            dist = i - last_seen[x]
            if dist < min_dist:
                min_dist = dist
        last_seen[x] = i
        
    print(min_dist if min_dist != float("inf") else -1)

if __name__ == "__main__":
    solve()
