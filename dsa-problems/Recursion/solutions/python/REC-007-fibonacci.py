def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    import sys
    n = int(sys.stdin.read().strip())
    print(fibonacci(n))

if __name__ == "__main__":
    main()
