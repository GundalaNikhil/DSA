import sys

def maximize_or_with_k_picks(a: list[int], k: int) -> int:
    n = len(a)
    # Optimization: If K is large enough, we can set all possible bits
    if k >= 30:
        total = 0
        for x in a:
            total |= x
        return total
        
    current_or = 0
    used = [False] * n
    
    for _ in range(k):
        best_or = -1
        best_idx = -1
        
        for i in range(n):
            if not used[i]:
                new_or = current_or | a[i]
                if new_or > best_or:
                    best_or = new_or
                    best_idx = i
                    
        # If we found something (which we always should if k <= n)
        if best_idx != -1:
            current_or = best_or
            used[best_idx] = True
            
    return current_or

def main():
    input_data = sys.stdin.read()
    data = input_data.split()
    if not data: return
    
    ptr = 0
    n = int(data[ptr]); ptr += 1
    a = []
    for _ in range(n):
        a.append(int(data[ptr])); ptr += 1
    
    k = int(data[ptr]); ptr += 1
    
    result = maximize_or_with_k_picks(a, k)
    print(result)

if __name__ == "__main__":
    main()
