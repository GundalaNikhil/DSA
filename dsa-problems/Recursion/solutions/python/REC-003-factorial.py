def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def main():
    import sys
    n = int(sys.stdin.read().strip())
    print(factorial(n))

if __name__ == "__main__":
    main()
