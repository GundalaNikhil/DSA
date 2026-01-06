import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        w = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))
    except StopIteration:
        return

    
    counts = {}
    ans = []
    
    for i in range(n):
        val = a[i]
        counts[val] = counts.get(val, 0) + 1
        
        # Remove old
        if i >= w:
            old_val = a[i - w]
            counts[old_val] -= 1
            if counts[old_val] == 0:
                del counts[old_val]
                
        # Check window validity
        if i >= w - 1:
            best = -1
            
            for v, c in counts.items():
                if c > w // 2:
                    best = v
                    break
            ans.append(best)
            
    print(*(ans))

if __name__ == "__main__":
    solve()
