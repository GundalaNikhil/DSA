import sys
import heapq


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    rows = int(input_data[ptr])
    ptr += 1
    cols = int(input_data[ptr])
    ptr += 1
    turn_penalty = int(input_data[ptr])
    ptr += 1
    grid = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(int(input_data[ptr]))
            ptr += 1
            grid.append(row)
            start_r = int(input_data[ptr])
            ptr += 1
            start_c = int(input_data[ptr])
            ptr += 1
            end_r = int(input_data[ptr])
            ptr += 1
            end_c = int(input_data[ptr])
            ptr += 1
            dr = [-1, 0, 1, 0]
            dc = [0, 1, 0, -1]
            pq = [(0, start_r, start_c, -1)]
            dist = {}
            while pq:
                d, r, c, ldir = heapq.heappop(pq)
                if (r, c, ldir) in dist and dist[(r, c, ldir)] <= d:
                    continue
                dist[(r, c, ldir)] = d
                if r == end_r and c == end_c:
                    print(d)
                    return
                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]
                    if 0 <= nr < rows and 0 <= nc < cols:
                        move_cost = grid[nr][nc]
                        if ldir != -1 and ldir != i:
                            move_cost += turn_penalty
                            if (nr, nc, i) not in dist or dist[
                                (nr, nc, i)
                            ] > d + move_cost:
                                heapq.heappush(pq, (d + move_cost, nr, nc, i))
                                print("-1")


if __name__ == "__main__":
    solve()
