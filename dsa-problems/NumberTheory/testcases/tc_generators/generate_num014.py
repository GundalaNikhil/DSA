import sys
import random
import math

def gcd(a, b):
    return math.gcd(a, b)

def solve(n, L, points):
    if not points: return 0
    
    # Handle duplicate points
    point_map = {}
    for p in points:
        point_map[p] = point_map.get(p, 0) + 1
    
    max_count = max(point_map.values())
    
    unique_points = list(point_map.keys())
    m = len(unique_points)
    if m <= 1:
        return max_count
    
    for i in range(m):
        x1, y1 = unique_points[i]
        slopes = {}
        for j in range(m):
            if i == j: continue
            x2, y2 = unique_points[j]
            dx = x2 - x1
            dy = y2 - y1
            g = gcd(abs(dx), abs(dy))
            dx //= g
            dy //= g
            if dx < 0 or (dx == 0 and dy < 0):
                dx = -dx
                dy = -dy
            
            slope = (dx, dy)
            if slope not in slopes:
                slopes[slope] = []
            
            dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            # Use dot product to determine sign along the line
            # Vector v is (dx, dy). j-i is (orig_dx, orig_dy).
            orig_dx = x2-x1
            orig_dy = y2-y1
            if orig_dx * dx + orig_dy * dy < 0:
                dist = -dist
            
            slopes[slope].append((dist, point_map[unique_points[j]]))
            
        for slope in slopes:
            group = slopes[slope]
            # Add the anchor point itself
            group.append((0.0, point_map[unique_points[i]]))
            group.sort()
            
            # Sliding window per slope
            left = 0
            current_sum = 0
            for right in range(len(group)):
                current_sum += group[right][1]
                while group[right][0] - group[left][0] > L + 1e-9:
                    current_sum -= group[left][1]
                    left += 1
                max_count = max(max_count, current_sum)
                
    return max_count

def make_test_case(n, L, points):
    res = solve(n, L, points)
    inp = f"{n} {L}\n" + "\n".join(f"{x} {y}" for x, y in points)
    out = str(res)
    return {"input": inp, "output": out}

def print_case(c):
    print("  - input: |-")
    for line in c["input"].split("\n"):
        print(f"      {line}")
    print("    output: |-")
    for line in c["output"].split("\n"):
        print(f"      {line}")

def main():
    tc = {
        "problem_id": "NUM_MAXIMUM_POINTS_LINE_SEGMENT_LIMIT__2904",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    tc["samples"].append(make_test_case(4, 2, [(0, 0), (1, 1), (2, 2), (0, 1)]))

    # Public
    tc["public"].append(make_test_case(3, 10, [(0, 0), (10, 0), (20, 0)]))
    tc["public"].append(make_test_case(2, 1, [(0, 0), (0, 1)]))

    # Hidden
    # Edge Cases
    tc["hidden"].append(make_test_case(1, 10, [(0, 0)]))
    tc["hidden"].append(make_test_case(2, 10**6, [(-10**6, -10**6), (10**6, 10**6)]))
    tc["hidden"].append(make_test_case(3, 1, [(0, 0), (0, 0), (0, 0)]))

    # Boundary Cases
    tc["hidden"].append(make_test_case(5, 5, [(0, 0), (3, 4), (6, 8), (9, 12), (0, 5)]))

    # Normal Cases
    for _ in range(5):
        n = random.randint(10, 50)
        L = random.randint(1, 100)
        points = [(random.randint(-100, 100), random.randint(-100, 100)) for _ in range(n)]
        tc["hidden"].append(make_test_case(n, L, points))

    # Special Case (Vertical/Horizontal lines)
    tc["hidden"].append(make_test_case(10, 5, [(i, 0) for i in range(10)]))
    tc["hidden"].append(make_test_case(10, 5, [(0, i) for i in range(10)]))

    # Stress Case
    n_stress = 500
    L_stress = 1000
    points_stress = [(random.randint(-1000, 1000), random.randint(-1000, 1000)) for _ in range(n_stress)]
    tc["hidden"].append(make_test_case(n_stress, L_stress, points_stress))

    print(f"problem_id: {tc['problem_id']}")
    for section in ["samples", "public", "hidden"]:
        print(f"\n{section}:")
        for c in tc[section]:
            print_case(c)

if __name__ == "__main__":
    main()
