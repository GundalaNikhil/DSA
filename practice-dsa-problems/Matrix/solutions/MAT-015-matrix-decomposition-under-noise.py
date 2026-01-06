import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    a = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(int(input_data[ptr]))
            ptr += 1
            a.append(row)
            
    b = [[0] * n for _ in range(n)]
    total_error = 0
    for i in range(n):
        for j in range(i, n):
            if i == j:
                b[i][j] = a[i][j]
            else:
                val = min(a[i][j], a[j][i])
                b[i][j] = b[j][i] = val
                total_error += abs(a[i][j] - val) + abs(a[j][i] - val)
                
    print(total_error)
    for row in b:
        print(*(row))


if __name__ == "__main__":
    solve()
