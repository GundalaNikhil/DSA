from collections import deque
import random
import yaml

def solve(r, c, grid):
    queue = deque()
    unlit = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                queue.append((i, j, 0))
            else:
                unlit += 1
                
    if unlit == 0:
        return 0
    if not queue:
        return -1
        
    max_dist = 0
    visited = [[False]*c for _ in range(r)]
    for i, j, d in queue:
        visited[i][j] = True
        
    while queue:
        curr_r, curr_c, d = queue.popleft()
        max_dist = max(max_dist, d)
        
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = curr_r + dr, curr_c + dc
            if 0 <= nr < r and 0 <= nc < c and not visited[nr][nc] and grid[nr][nc] == 0:
                visited[nr][nc] = True
                unlit -= 1
                queue.append((nr, nc, d + 1))
                
    return max_dist if unlit == 0 else -1

def make_test_case(grid):
    r = len(grid)
    c = len(grid[0])
    res = solve(r, c, grid)
    input_str = f"{r} {c}\n" + "\n".join(" ".join(map(str, row)) for row in grid)
    output_str = str(res)
    return {"input": input_str, "output": output_str}

def generate_yaml():
    tc = {
        "samples": [
            make_test_case([
                [1, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 1]
            ])
        ],
        "public": [
            make_test_case([[1, 1], [1, 1]]),
            make_test_case([[0, 0], [0, 0]]),
            make_test_case([[1, 0], [0, 0]])
        ],
        "hidden": []
    }

    # Edge cases: 1x1, 1xC, Rx1
    tc["hidden"].append(make_test_case([[1]]))
    tc["hidden"].append(make_test_case([[0]]))
    tc["hidden"].append(make_test_case([[1, 0, 0, 1]]))
    tc["hidden"].append(make_test_case([[1], [0], [0]]))
    
    # Large sequence
    r_large, c_large = 200, 200
    grid_large = [[0]*c_large for _ in range(r_large)]
    grid_large[0][0] = 1
    tc["hidden"].append(make_test_case(grid_large))

    # All unlit
    tc["hidden"].append(make_test_case([[0]*10 for _ in range(10)]))

    # All lit
    tc["hidden"].append(make_test_case([[1]*10 for _ in range(10)]))

    # Stress case: random grid
    grid_rand = [[random.choice([0, 1]) for _ in range(200)] for _ in range(200)]
    tc["hidden"].append(make_test_case(grid_rand))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
