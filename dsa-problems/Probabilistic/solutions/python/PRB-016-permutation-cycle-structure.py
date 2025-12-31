import sys

def cycle_expectations(n: int, k: int):
    expected_cycles_k = 1.0 / k
    expected_longest = n * 0.624330
    return expected_cycles_k, expected_longest

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])
    
    res = cycle_expectations(n, k)
    print(f"{res[0]:.6f} {res[1]:.6f}")

if __name__ == "__main__":
    main()
