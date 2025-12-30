def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    import sys
    input_data = sys.stdin.read().strip()
    n = int(input_data)
    
    if is_prime(n):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
