import sys

def swap_adjacent_2bit_blocks(x: int) -> int:
    # Python ints are arbitrary precision. Use 32-bit mask.
    MASK_32 = 0xFFFFFFFF
    x &= MASK_32
    
    even_mask = 0x33333333
    odd_mask = 0xCCCCCCCC
    
    even_blocks = x & even_mask
    odd_blocks = x & odd_mask
    
    # Even blocks move left (<< 2)
    # Odd blocks move right (>> 2)
    res = (even_blocks << 2) | (odd_blocks >> 2)
    
    return res & MASK_32

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    x = int(data[0])
    
    result = swap_adjacent_2bit_blocks(x)
    print(result)

if __name__ == "__main__":
    main()
