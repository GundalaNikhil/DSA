from typing import List

def weighted_area(x1: List[int], y1: List[int], x2: List[int], y2: List[int], w: List[int], W: int) -> int:
    n = len(x1)
    if n == 0:
        return 0
        
    nx1, ny1, nx2, ny2 = [], [], [], []
    for i in range(n):
        nx1.append(min(x1[i], x2[i]))
        nx2.append(max(x1[i], x2[i]))
        ny1.append(min(y1[i], y2[i]))
        ny2.append(max(y1[i], y2[i]))
        
    xs = sorted(list(set(nx1 + nx2)))
    ys = sorted(list(set(ny1 + ny2)))
    
    total_area = 0
    for i in range(len(xs) - 1):
        x_start, x_end = xs[i], xs[i+1]
        width = x_end - x_start
        if width <= 0: continue
        
        # Which rectangles cover this vertical strip?
        strip_rects = []
        for j in range(n):
            if nx1[j] <= x_start and nx2[j] >= x_end:
                strip_rects.append(j)
        
        if not strip_rects:
            continue
            
        # For this strip, find intervals on Y
        y_weights = [0] * (len(ys) - 1)
        for rid in strip_rects:
            y_s, y_e = ny1[rid], ny2[rid]
            # Find which intervals [ys[k], ys[k+1]) are covered
            # We can use binary search or just a loop since N is small
            for k in range(len(ys) - 1):
                if ys[k] >= y_s and ys[k+1] <= y_e:
                    y_weights[k] += w[rid]
        
        strip_len = 0
        for k in range(len(ys) - 1):
            if y_weights[k] >= W:
                strip_len += ys[k+1] - ys[k]
        
        total_area += strip_len * width
        
    return total_area

def main() -> None:
    import sys
    # Increase recursion depth for deep segment tree
    sys.setrecursionlimit(200000)
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        m = int(next(it))
        if m == 0:
            return
        W = int(next(it))
        x1, y1, x2, y2, w = [], [], [], [], []
        for _ in range(m):
            x1.append(int(next(it)))
            y1.append(int(next(it)))
            x2.append(int(next(it)))
            y2.append(int(next(it)))
            w.append(int(next(it)))
        print(weighted_area(x1, y1, x2, y2, w, W))
    except StopIteration:
        return

if __name__ == "__main__":
    main()
