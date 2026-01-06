import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        matrix = []
        for _ in range(n):
            row = []
            for _ in range(m):
                row.append(int(next(iterator)))
            matrix.append(row)
    except StopIteration:
        return

    
    max_sum = -float("inf")
    
    for top in range(n):
        col_sums = [0] * m
        for bottom in range(top, n):
            # Update col_sums by adding new row
            for j in range(m):
                col_sums[j] += matrix[bottom][j]
                
            # Kadane's on col_sums
            curr_max = 0
            kadane_max = -float("inf")
            
            for x in col_sums:
                curr_max += x
                if curr_max > kadane_max:
                    kadane_max = curr_max
                if curr_max < 0:
                    curr_max = 0
                    
            if kadane_max > max_sum:
                max_sum = kadane_max
                
    print(max_sum)

if __name__ == "__main__":
    solve()
