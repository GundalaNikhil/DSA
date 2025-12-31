from typing import List, Tuple

def weighted_area(x1: List[int], y1: List[int], x2: List[int], y2: List[int], w: List[int], W: int) -> int:
    n = len(x1)
    ys = sorted(set(y1 + y2))
    # Coordinate compression map for Y
    ymap = {y: i for i, y in enumerate(ys)}
    
    events = []
    for i in range(n):
        events.append((x1[i], 1, y1[i], y2[i], w[i]))
        events.append((x2[i], -1, y1[i], y2[i], w[i]))
    events.sort()
    
    m = len(ys) - 1
    if m == 0:
        return 0
        
    
    cnt = [0] * (4 * m)
    
    weights = [0] * m
    widths = [ys[i+1] - ys[i] for i in range(m)]
    
    prev_x = events[0][0]
    total_area = 0
    
    curr_weights = [0]*m
    
    # Robust O(N^2) with small constant
    for i, (x, typ, y1_val, y2_val, wt) in enumerate(events):
        if i > 0:
            width = x - prev_x
            if width > 0:
                # Add coverage
                # Bottleneck loop
                covered = 0
                for j in range(m):
                    if curr_weights[j] >= W:
                        covered += widths[j]
                total_area += covered * width
        
        # Update weights
        idx_l = ymap[y1_val]
        idx_r = ymap[y2_val]
        val = wt * typ
        for j in range(idx_l, idx_r):
            curr_weights[j] += val
            
        prev_x = x
        
    return total_area

def main() -> None:
    import sys
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    try:
        m = next(it)
        W = next(it)
        x1=[]; y1=[]; x2=[]; y2=[]; w=[]
        for _ in range(m):
            x1.append(next(it)); y1.append(next(it)); x2.append(next(it)); y2.append(next(it)); w.append(next(it))
        print(weighted_area(x1, y1, x2, y2, w, W))
    except StopIteration:
        return

if __name__ == "__main__":
    main()
