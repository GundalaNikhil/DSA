from typing import List
import math

def largest_quiet_circle(xL: int, yB: int, xR: int, yT: int, xs: List[int], ys: List[int], rs: List[int]) -> float:
    n = len(xs)
    
    def get_radius(x, y):
        # Distance to borders
        r = min(x - xL, xR - x, y - yB, yT - y)
        if r <= 0: return 0.0
        
        # Distance to each noise disk
        # dist(C, Pi) >= R + ri  =>  R <= dist(C, Pi) - ri
        for i in range(n):
            d = math.sqrt((x - xs[i])**2 + (y - ys[i])**2)
            r = min(r, d - rs[i])
            if r <= 0: return 0.0
        return r

    best_r = 0.0
    cands = []
    
    # 1. Broad sampling: Grid + Key Points
    grid_res = 120
    # Add grid
    for i in range(grid_res + 1):
        cx = xL + (xR - xL) * i / float(grid_res)
        for j in range(grid_res + 1):
            cy = yB + (yT - yB) * j / float(grid_res)
            r = get_radius(cx, cy)
            if r > 0: cands.append((r, cx, cy))
    
    # Add midpoints and edge projections
    for i in range(n):
        cands.append((get_radius(xs[i], yB), xs[i], yB))
        cands.append((get_radius(xs[i], yT), xs[i], yT))
        cands.append((get_radius(xL, ys[i]), xL, ys[i]))
        cands.append((get_radius(xR, ys[i]), xR, ys[i]))
        for j in range(i+1, n):
            mx, my = (xs[i]+xs[j])/2.0, (ys[i]+ys[j])/2.0
            cands.append((get_radius(mx, my), mx, my))

    if not cands:
        mid_x, mid_y = (xL + xR) / 2.0, (yB + yT) / 2.0
        best_r = max(best_r, get_radius(mid_x, mid_y))
    else:
        cands.sort(reverse=True)
        # 2. Hill Climbing from top candidates
        seen_starts = set()
        count = 0
        for _, sx, sy in cands:
            if count >= 60: break
            # Simple deduplication
            grid_coord = (round(sx*10), round(sy*10))
            if grid_coord in seen_starts: continue
            seen_starts.add(grid_coord)
            count += 1
            
            curr_x, curr_y = sx, sy
            curr_r = get_radius(curr_x, curr_y)
            
            step = max(xR - xL, yT - yB) / float(grid_res)
            while step > 1e-13:
                improved = False
                for dx, dy in [(0,1), (0,-1), (1,0), (-1,0), (0.7,0.7), (0.7,-0.7), (-0.7,0.7), (-0.7,-0.7), (0.3,0.9), (0.9,0.3)]:
                    nx, ny = curr_x + dx * step, curr_y + dy * step
                    if xL <= nx <= xR and yB <= ny <= yT:
                        nr = get_radius(nx, ny)
                        if nr > curr_r:
                            curr_r, curr_x, curr_y = nr, nx, ny
                            improved = True
                if not improved:
                    step *= 0.5
            best_r = max(best_r, curr_r)
            
    return max(0.0, best_r)

def main() -> None:
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    try:
        xL, yB, xR, yT, n = map(int, [next(it), next(it), next(it), next(it), next(it)])
        xs, ys, rs = [], [], []
        for _ in range(n):
            xs.append(int(next(it)))
            ys.append(int(next(it)))
            rs.append(int(next(it)))
        r = largest_quiet_circle(xL, yB, xR, yT, xs, ys, rs)
        print(f"{r:.6f}")
    except (StopIteration, ValueError):
        return

if __name__ == "__main__":
    main()
