import sys

def toggle_ranges_min_flips(A: list[int], B: list[int]) -> int:
    count = 0
    prev_diff = 0
    
    for a_val, b_val in zip(A, B):
        curr_diff = a_val ^ b_val
        if curr_diff == 1 and prev_diff == 0:
            count += 1
        prev_diff = curr_diff
        
    return count

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    ptr = 0
    n = int(data[ptr]); ptr += 1
    A = []
    for _ in range(n):
        A.append(int(data[ptr])); ptr += 1
    B = []
    for _ in range(n):
        B.append(int(data[ptr])); ptr += 1
        
    result = toggle_ranges_min_flips(A, B)
    print(result)

if __name__ == "__main__":
    main()
