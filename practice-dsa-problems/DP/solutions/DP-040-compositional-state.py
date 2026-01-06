import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    X = int(input_data[ptr])
    ptr += 1
    Y = int(input_data[ptr])
    ptr += 1
    a_count = int(input_data[ptr])
    ptr += 1
    actions = []
    for _ in range(a_count):
        dx = int(input_data[ptr])
        ptr += 1
        dy = int(input_data[ptr])
        ptr += 1
        r = int(input_data[ptr])
        ptr += 1
        actions.append((dx, dy, r))
        inf = float("inf")
        dp = [[-inf] * (Y + 1) for _ in range(X + 1)]
        dp[0][0] = 0
        for _ in range(n):
            new_dp = [[-inf] * (Y + 1) for _ in range(X + 1)]
            for x in range(X + 1):
                for y in range(Y + 1):
                    if dp[x][y] == -inf:
                        continue
                    for dx, dy, r in actions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx <= X and 0 <= ny <= Y:
                            new_dp[nx][ny] = max(new_dp[nx][ny], dp[x][y] + r)
            dp = new_dp
        
    ans = -inf
    for x in range(X + 1):
        for y in range(Y + 1):
            ans = max(ans, dp[x][y])
            
    print(ans if ans != -inf else -1)


if __name__ == "__main__":
    solve()
