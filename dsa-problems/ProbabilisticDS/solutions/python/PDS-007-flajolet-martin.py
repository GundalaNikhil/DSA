import sys

def estimate_distinct(R: int) -> float:
    return (2 ** R) / 0.77351

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    R = int(data[0])
    print(f"{estimate_distinct(R):.6f}")

if __name__ == "__main__":
    main()
