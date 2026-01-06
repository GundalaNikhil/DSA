import sys
def get_rank(matrix):
    if not matrix:
        return 0
    # get_rank definition moved below or used from scope? 
    # Original file had `get_rank` at top but with broken logic inside loop.
    # We should fix it at top level if possible, but `solve` is using it.
    # The replacement above fixes the call site.
    # This replacement fixes the definition at the top.
    
    n = len(matrix)
    m = len(matrix[0])
    mat = [row[:] for row in matrix]
    rank = 0
    pivot_row = 0
    eps = 1e-9
    
    for j in range(m):
        if pivot_row >= n:
            break
        sel = pivot_row
        for i in range(pivot_row, n):
            if abs(mat[i][j]) > abs(mat[sel][j]):
                sel = i
                
        if abs(mat[sel][j]) < eps:
            continue
            
        mat[sel], mat[pivot_row] = mat[pivot_row], mat[sel]
        
        for i in range(n):
            if i != pivot_row:
                factor = mat[i][j] / mat[pivot_row][j]
                for k in range(j, m):
                    mat[i][k] -= factor * mat[pivot_row][k]
                    
        pivot_row += 1
        rank += 1
        
    return rank
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
            row.append(float(input_data[ptr]))
            ptr += 1
            matrix.append(row)
            matrix.append(row)
            
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        if op == 'SWAP':
            r1 = int(input_data[ptr]) - 1
            ptr += 1
            r2 = int(input_data[ptr]) - 1
            ptr += 1
            matrix[r1], matrix[r2] = matrix[r2], matrix[r1]
        elif op == 'SET':
            r = int(input_data[ptr]) - 1
            ptr += 1
            new_row = []
            for _ in range(m):
                new_row.append(float(input_data[ptr]))
                ptr += 1
            matrix[r] = new_row
        elif op == 'ADD':
            r1 = int(input_data[ptr]) - 1
            ptr += 1
            r2 = int(input_data[ptr]) - 1
            ptr += 1
            for j in range(m):
                matrix[r1][j] += matrix[r2][j]
                
        # Calculate Rank
        # Note: Re-calculating rank after each op as per code structure.
        print(get_rank(matrix))

def get_rank(matrix):
    if not matrix:
        return 0
    n = len(matrix)
    m = len(matrix[0])
    mat = [row[:] for row in matrix] # Copy
    rank = 0
    pivot_row = 0
    eps = 1e-9
    
    for j in range(m):
        if pivot_row >= n:
            break
            
        # Select pivot
        sel = pivot_row
        for i in range(pivot_row, n):
            if abs(mat[i][j]) > abs(mat[sel][j]):
                sel = i
                
        if abs(mat[sel][j]) < eps:
            continue
            
        mat[sel], mat[pivot_row] = mat[pivot_row], mat[sel]
        
        # Eliminate
        # Standard Gaussian: iterate i > pivot_row
        # Or Jordan (all update)? Code was weird.
        # Standard rank bounds:
        for i in range(n):
            if i != pivot_row:
                factor = mat[i][j] / mat[pivot_row][j]
                for k in range(j, m):
                    mat[i][k] -= factor * mat[pivot_row][k]
                    
        pivot_row += 1
        rank += 1
        
    return rank
if __name__ == '__main__':
    solve()