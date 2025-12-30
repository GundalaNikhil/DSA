import sys

def hit_probability(a: int, b: int, T: int) -> float:
    if a == 0 and b == 0:
        return 1.0
        
    offset = T
    size = 2 * T + 1
    dp = [[0.0] * size for _ in range(size)]
    
    start_x, start_y = offset, offset
    target_x, target_y = a + offset, b + offset
    
    dp[start_x][start_y] = 1.0
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    for t in range(1, T + 1):
        next_dp = [[0.0] * size for _ in range(size)]
        
        # Carry over absorbed probability
        next_dp[target_x][target_y] = dp[target_x][target_y]
        
        min_val = offset - (t - 1)
        max_val = offset + (t - 1)
        
        # Clamp bounds
        min_val = max(0, min_val)
        max_val = min(size - 1, max_val)
        
        for x in range(min_val, max_val + 1):
            for y in range(min_val, max_val + 1):
                if dp[x][y] == 0:
                    continue
                if x == target_x and y == target_y:
                    continue
                    
                prob = dp[x][y] * 0.25
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    next_dp[nx][ny] += prob
                    
        dp = next_dp
        
    return dp[target_x][target_y]

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    a = int(data[0])
    b = int(data[1])
    T = int(data[2])
    print(f"{hit_probability(a, b, T):.6f}")

if __name__ == "__main__":
    main()
