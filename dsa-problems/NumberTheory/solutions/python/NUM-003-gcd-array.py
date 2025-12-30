def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    import sys
    input_data = sys.stdin.read().strip().split()
    n = int(input_data[0])
    arr = [int(input_data[i]) for i in range(1, n + 1)]
    
    result = arr[0]
    for i in range(1, n):
        result = gcd(result, arr[i])
    
    print(result)

if __name__ == "__main__":
    main()
