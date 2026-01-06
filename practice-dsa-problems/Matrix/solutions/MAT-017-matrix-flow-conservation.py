import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    q = int(input_data[ptr])
    ptr += 1
    matrix = []
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append(int(input_data[ptr]))
            ptr += 1
            matrix.append(row)
            matrix.append(row)
            
    for i in range(1, q + 1):
        r1 = int(input_data[ptr]) - 1
        ptr += 1
        c1 = int(input_data[ptr]) - 1
        ptr += 1
        r2 = int(input_data[ptr]) - 1
        ptr += 1
        c2 = int(input_data[ptr]) - 1
        ptr += 1
        x = int(input_data[ptr])
        ptr += 1
        
        if abs(r1 - r2) + abs(c1 - c2) != 1:
            print(i)
            return
            
        if matrix[r1][c1] < x:
            print(i)
            return
            
        matrix[r1][c1] -= x
        matrix[r2][c2] += x
        
    print(0)
    for row in matrix:
        print(*(row))


if __name__ == "__main__":
    solve()
