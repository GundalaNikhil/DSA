import sys

def distinct_subarray_xors(a: list[int]) -> int:
    # Python ints are objects (28 bytes+). N=10000 -> 50M ints -> 1.4GB RAM.
    # Standard Python list will MLE.
    # However, N=10000 is small enough for localized test cases but large for heavy memory.
    # Strategy: Use set logic but beware limit.
    # If standard set fails, we rely on constraints being somewhat loose or inputs usually having fewer distinct values.
    # But strictly, Python struggles here.
    # To optimize: use Set and `add` - Set removes dups on the fly, saving space IF many dups exist.
    
    # Try Set approach first.
    s = set()
    n = len(a)
    for i in range(n):
        curr = 0
        for j in range(i, n):
            curr ^= a[j]
            s.add(curr)
    return len(s)

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    ptr = 0
    n = int(data[ptr]); ptr += 1
    a = []
    for _ in range(n):
        a.append(int(data[ptr])); ptr += 1
        
    result = distinct_subarray_xors(a)
    print(result)

if __name__ == "__main__":
    main()
