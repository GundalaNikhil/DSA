import sys

def minimal_product_split(x: int) -> int:
    s = str(x)
    n = len(s)
    min_prod = float('inf')
    
    for i in range(1, n):
        a = int(s[:i])
        b = int(s[i:])
        prod = a * b
        if prod > 0:
            min_prod = min(min_prod, prod)
            
    return min_prod

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    x = int(data[0])
    print(minimal_product_split(x))

if __name__ == "__main__":
    main()
