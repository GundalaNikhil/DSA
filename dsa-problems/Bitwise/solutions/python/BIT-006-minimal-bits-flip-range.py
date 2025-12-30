import sys

def minimal_bits_flip_range(x: int, y: int) -> int:
    diff = x ^ y
    if diff == 0: return 0
    
    # Check if diff is 2^m - 1
    if (diff & (diff + 1)) == 0:
        return diff.bit_length()
        
    return -1

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    x = int(data[0])
    y = int(data[1])
    
    result = minimal_bits_flip_range(x, y)
    print(result)

if __name__ == "__main__":
    main()
