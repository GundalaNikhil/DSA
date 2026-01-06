import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    S = int(input_data[ptr])
    ptr += 1
    states = []
    for _ in range(n):
        states.append(int(input_data[ptr]))
        ptr += 1
        
    matrix = []
    for _ in range(S):
        row = []
        for _ in range(S):
            row.append(int(input_data[ptr]))
            ptr += 1
        matrix.append(row)
        
    q = int(input_data[ptr])
    ptr += 1
    
    invalid_pairs = 0
    for i in range(n - 1):
        if matrix[states[i]][states[i + 1]] == 0:
            invalid_pairs += 1
            
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        pos = int(input_data[ptr])
        ptr += 1
        x = int(input_data[ptr])
        ptr += 1
        
        idx = pos - 1
        if idx > 0:
            if matrix[states[idx - 1]][states[idx]] == 0:
                invalid_pairs -= 1
        if idx < n - 1:
            if matrix[states[idx]][states[idx + 1]] == 0:
                invalid_pairs -= 1
                
        states[idx] = x
        
        if idx > 0:
            if matrix[states[idx - 1]][states[idx]] == 0:
                invalid_pairs += 1
        if idx < n - 1:
            if matrix[states[idx]][states[idx + 1]] == 0:
                invalid_pairs += 1
                
        if invalid_pairs == 0:
            print("VALID")
        else:
            print("INVALID")
