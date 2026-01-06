import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    weights = []
    for _ in range(n):
        weights.append(int(input_data[ptr]))
        ptr += 1
        
    biases = []
    for _ in range(n):
        biases.append(int(input_data[ptr]))
        ptr += 1
        
    x = int(input_data[ptr])
    ptr += 1
    y = int(input_data[ptr])
    ptr += 1
    
    curr_val = x
    for i in range(n):
        curr_val = max(0, curr_val * weights[i] + biases[i])
        if curr_val > 10**18:
            break
            
    print(f"{curr_val} {(curr_val - y)**2}")


if __name__ == "__main__":
    solve()
