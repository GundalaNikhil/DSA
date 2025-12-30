import sys

def bitwise_and_skip_multiples(L: int, R: int, m: int) -> int:
    # Small range optimization
    if R - L <= 2000000:
        ans = -1
        found = False
        for i in range(L, R + 1):
            if i % m != 0:
                ans &= i
                found = True
        return ans if found else -1

    # Large range: Use Common Prefix logic
    shift = 0
    l_temp = L
    r_temp = R
    
    while l_temp != r_temp:
        l_temp >>= 1
        r_temp >>= 1
        shift += 1
        
    standard_and = l_temp << shift
    
    # Correction for m=2 (skipping evens)
    if m == 2:
        standard_and |= 1
        
    return standard_and

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    L = int(data[0])
    R = int(data[1])
    m = int(data[2])
    
    result = bitwise_and_skip_multiples(L, R, m)
    print(result)

if __name__ == "__main__":
    main()
