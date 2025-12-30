def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    return x * power(x, n - 1)

def main():
    import sys
    input_data = sys.stdin.read().strip().split()
    x = float(input_data[0])
    n = int(input_data[1])
    print(power(x, n))

if __name__ == "__main__":
    main()
