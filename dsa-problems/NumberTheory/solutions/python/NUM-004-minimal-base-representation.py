import sys

def get_digit_sum(x: int, b: int) -> int:
    total = 0
    while x > 0:
        total += x % b
        x //= b
    return total

def minimal_base(x: int):
    min_sum = float('inf')
    best_base = 2
    
    for b in range(2, 37):
        current_sum = get_digit_sum(x, b)
        if current_sum < min_sum:
            min_sum = current_sum
            best_base = b
            
    return best_base, min_sum

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    x = int(data[0])
    b, s = minimal_base(x)
    print(f"{b} {s}")

if __name__ == "__main__":
    main()
