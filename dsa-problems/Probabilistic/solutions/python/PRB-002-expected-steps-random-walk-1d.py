import sys

def expected_steps(a: int, b: int, p: float) -> float:
    if abs(p - 0.5) < 1e-9:
        return float(a * b)

    q = 1.0 - p
    r = q / p
    M = a + b
    z = b

    term1 = z / (q - p)
    term2 = (M / (q - p)) * ((1.0 - pow(r, z)) / (1.0 - pow(r, M)))

    return term1 - term2

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    a = int(data[0])
    b = int(data[1])
    p = float(data[2])
    print(f"{expected_steps(a, b, p):.6f}")

if __name__ == "__main__":
    main()
