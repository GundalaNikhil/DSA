import sys

def count_set_bits_indexed_xor(a: list[int]) -> int:
    total = 0
    for i, x in enumerate(a):
        # bin().count() is the standard Pythonic way
        total += (i ^ x).bit_count() # Python 3.10+
        # For older python: bin(i ^ x).count('1')
        
    return total

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    ptr = 0
    n = int(data[ptr]); ptr += 1
    a = []
    for _ in range(n):
        a.append(int(data[ptr])); ptr += 1
    
    result = count_set_bits_indexed_xor(a)
    print(result)

if __name__ == "__main__":
    main()
