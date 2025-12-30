import sys
from math import gcd, sqrt

def max_points_on_segment(points, L):
    n = len(points)
    if n <= 1: return n
    
    point_counts = {}
    for p in points:
        point_counts[p] = point_counts.get(p, 0) + 1
        
    unique_pts = list(point_counts.keys())
    counts = [point_counts[p] for p in unique_pts]
    m = len(unique_pts)
    
    max_pts = max(counts)
    
    for i in range(m):
        slope_map = {}
        x1, y1 = unique_pts[i]
        
        for j in range(m):
            if i == j: continue
            x2, y2 = unique_pts[j]
            
            dx = x2 - x1
            dy = y2 - y1
            dist = sqrt(dx*dx + dy*dy)
            
            if dist > L + 1e-9:
                continue
                
            g = gcd(abs(dx), abs(dy))
            slope = (dx // g, dy // g)
            
            slope_map[slope] = slope_map.get(slope, 0) + counts[j]
            
        for count in slope_map.values():
            max_pts = max(max_pts, counts[i] + count)
            
    return max_pts

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        L = int(next(it))
        points = []
        for _ in range(n):
            x = int(next(it))
            y = int(next(it))
            points.append((x, y))
            
        print(max_points_on_segment(points, L))
    except (StopIteration, ValueError):
        pass

if __name__ == "__main__":
    main()
