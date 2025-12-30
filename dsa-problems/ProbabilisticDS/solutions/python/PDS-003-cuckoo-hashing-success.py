import math
import sys

def success_probability(m: int, alpha: float) -> float:
    val = 1.0 - alpha
    exponent = -(val * val * m) / 2.0
    p_fail = math.exp(exponent)
    return 1.0 - p_fail

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    m = int(data[0])
    alpha = float(data[1])
    print(f"{success_probability(m, alpha):.6f}")

if __name__ == "__main__":
    main()
