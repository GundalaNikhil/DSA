import sys

def median_clt(n: int):
    mean = 0.5
    variance = 1.0 / (4 * n)
    return mean, variance

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    print(f"{0.5:.6f} {1.0/(4*n):.6f}")

if __name__ == "__main__":
    main()
