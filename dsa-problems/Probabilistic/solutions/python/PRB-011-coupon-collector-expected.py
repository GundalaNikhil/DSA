import sys

def expected_draws(N: int) -> float:
    harmonic_sum = 0.0
    for i in range(1, N + 1):
        harmonic_sum += 1.0 / i
    return N * harmonic_sum

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    N = int(data[0])
    print(f"{expected_draws(N):.6f}")

if __name__ == "__main__":
    main()
