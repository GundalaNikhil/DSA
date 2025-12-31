import sys

def subset_and_equals_x(a: list[int], X: int) -> int:
    # Filter candidates
    candidates = [v for v in a if (v & X) == X]
    n = len(candidates)
    
    count = 0
    limit = 1 << n
    
    for mask in range(1, limit):
        current_and = -1
        first = True
        
        for i in range(n):
            if (mask >> i) & 1:
                if first:
                    current_and = candidates[i]
                    first = False
                else:
                    current_and &= candidates[i]
        
        if not first and current_and == X:
            count += 1
            
    return count

def main():
    input_data = sys.stdin.read()
    data = input_data.split()
    if not data: return

    ptr = 0
    n = int(data[ptr]); ptr += 1
    a = []
    for _ in range(n):
        a.append(int(data[ptr])); ptr += 1

    X = int(data[ptr]); ptr += 1

    result = subset_and_equals_x(a, X)
    print(result)

if __name__ == "__main__":
    main()
