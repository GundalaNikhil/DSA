import math
import random
from typing import List, Tuple

EPS = 1e-12

def largest_empty_circle(xL: int, yB: int, xR: int, yT: int, xs: List[int], ys: List[int]) -> float:
    random.seed(1337)
    pts = list(zip(xs, ys))
    n = len(pts)

    def dist_sq(p, q):
        return (p[0]-q[0])**2 + (p[1]-q[1])**2

    def get_radius(x, y):
        # Distance to boundaries
        # If outside/on boundary, radius is 0 (or negative effectively)
        # We clamp point to be inside, but if checking arbitrary point
        if not (xL <= x <= xR and yB <= y <= yT): return 0.0
        r = min(x - xL, xR - x, y - yB, yT - y)
        if r <= EPS: return 0.0
        
        # Distance to nearest point
        # Optimization: brute force for small N
        min_d2 = float('inf')
        for px, py in pts:
            d2 = (x-px)**2 + (y-py)**2
            if d2 < min_d2: min_d2 = d2
            if d2 < r*r: # Early exit
                return math.sqrt(d2)
        return min(r, math.sqrt(min_d2))

    best_r = 0.0
    
    # 1. Check fixed candidates (Midpoints of P and Wall Projections)
    # Center = (px, (py+WallY)/2) etc.
    candidates = []
    candidates.append(((xL+xR)/2, (yB+yT)/2)) # Center of rect
    for px, py in pts:
        candidates.append((px, (py+yB)/2))
        candidates.append((px, (py+yT)/2))
        candidates.append(((px+xL)/2, py))
        candidates.append(((px+xR)/2, py))
    
    # Also midpoints between pairs (if N small)
    if n <= 100:
        for i in range(n):
            for j in range(i+1, n):
                candidates.append(((pts[i][0]+pts[j][0])/2, (pts[i][1]+pts[j][1])/2))

    # Evaluate initial candidates
    for cx, cy in candidates:
        r = get_radius(cx, cy)
        best_r = max(best_r, r)

    # 2. Simulated Annealing / Hill Climbing
    # Start from random positions (and best so far)
    starts = [(random.uniform(xL, xR), random.uniform(yB, yT)) for _ in range(10)]
    if candidates:
        # Add top 5 candidates as starts
        cand_with_score = []
        for cx, cy in candidates:
            cand_with_score.append((get_radius(cx, cy), cx, cy))
        cand_with_score.sort(reverse=True)
        for _, cx, cy in cand_with_score[:5]:
            starts.append((cx, cy))
            
    step_size = max(xR - xL, yT - yB) / 2.0
    precision = 1e-4
    
    for sx, sy in starts:
        curr_x, curr_y = sx, sy
        curr_r = get_radius(curr_x, curr_y)
        temp_step = step_size
        
        while temp_step > precision:
            # Try moving in 8 directions
            improved = False
            best_neigh_r = curr_r
            best_neigh_x, best_neigh_y = curr_x, curr_y
            
            # 8 neighbors
            dirs = [(0,1), (0,-1), (1,0), (-1,0), (0.7,0.7), (0.7,-0.7), (-0.7,0.7), (-0.7,-0.7)]
            random.shuffle(dirs) # Add randomness
            
            for dx, dy in dirs:
                nx = curr_x + dx * temp_step
                ny = curr_y + dy * temp_step
                # Clamp
                nx = max(xL, min(xR, nx))
                ny = max(yB, min(yT, ny))
                
                nr = get_radius(nx, ny)
                if nr > best_neigh_r:
                    best_neigh_r = nr
                    best_neigh_x, best_neigh_y = nx, ny
                    improved = True
            
            if improved:
                curr_x, curr_y = best_neigh_x, best_neigh_y
                curr_r = best_neigh_r
            else:
                temp_step *= 0.6 # Decrease step size
        
        best_r = max(best_r, curr_r)

    return best_r

def main() -> None:
    import sys
    import sys
    sys.setrecursionlimit(200000)
    def input_gen():
        for line in sys.stdin:
            for token in line.split():
                yield token
    it = input_gen()
    try:
        xL = int(next(it))
        yB = int(next(it))
        xR = int(next(it))
        yT = int(next(it))
        n = int(next(it))
        xs = []
        ys = []
        for _ in range(n):
            xs.append(int(next(it)))
            ys.append(int(next(it)))
        r = largest_empty_circle(xL, yB, xR, yT, xs, ys)
        print(f"{r:.6f}")
    except StopIteration:
        return

if __name__ == "__main__":
    main()
