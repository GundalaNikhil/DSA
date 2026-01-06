import sys
from collections import deque
import defaultdict


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    k = int(input_data[ptr])
    ptr += 1
    durations = []
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append(int(input_data[ptr]))
            ptr += 1
            durations.append(row)
            
    adj = defaultdict(list)
    in_degree = defaultdict(int)
    for _ in range(k):
        r1 = int(input_data[ptr]) - 1
        ptr += 1
        c1 = int(input_data[ptr]) - 1
        ptr += 1
        r2 = int(input_data[ptr]) - 1
        ptr += 1
        c2 = int(input_data[ptr]) - 1
        ptr += 1
        adj[(r1, c1)].append((r2, c2))
        in_degree[(r2, c2)] += 1
        
    dq = deque()
    dist = [[0] * m for _ in range(n)]
    
    for r in range(n):
        for c in range(m):
            if in_degree[(r, c)] == 0:
                dq.append((r, c))
                dist[r][c] = durations[r][c]
                
    count = 0
    while dq:
        r, c = dq.popleft()
        count += 1
        for nr, nc in adj[(r, c)]:
            dist[nr][nc] = max(dist[nr][nc], dist[r][c] + durations[nr][nc])
            in_degree[(nr, nc)] -= 1
            if in_degree[(nr, nc)] == 0:
                dq.append((nr, nc))
                
    if count < n * m:
        print("-1")
    else:
        max_time = 0
        for r in range(n):
            max_time = max(max_time, max(dist[r]))
        print(max_time)


if __name__ == "__main__":
    solve()
