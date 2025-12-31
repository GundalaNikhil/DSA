import sys

def max_subarray_xor_with_start(a: list[int], s: int) -> int:
    current_xor = 0
    max_xor = 0
    first = True
    
    for i in range(s, len(a)):
        current_xor ^= a[i]
        if first:
            max_xor = current_xor
            first = False
        else:
            if current_xor > max_xor:
                max_xor = current_xor
                
    return max_xor

def main():
    input_data = sys.stdin.read()
    data = input_data.split()
    if not data: return
    
    ptr = 0
    n = int(data[ptr]); ptr += 1
    a = []
    for _ in range(n):
        a.append(int(data[ptr])); ptr += 1
    
    s = int(data[ptr]); ptr += 1
    
    result = max_subarray_xor_with_start(a, s)
    print(result)

if __name__ == "__main__":
    main()
