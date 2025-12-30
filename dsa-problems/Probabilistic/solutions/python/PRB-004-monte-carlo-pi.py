import sys
import math

def estimate_pi(N: int, C: int):
    p_hat = C / N
    pi_hat = 4.0 * p_hat

    # Standard error of proportion
    std_err_p = math.sqrt(p_hat * (1.0 - p_hat) / N)

    # 95% Confidence Interval half-width
    error = 1.96 * std_err_p * 4.0

    return pi_hat, error

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    N = int(data[0])
    C = int(data[1])
    pi_hat, err = estimate_pi(N, C)
    print(f"{pi_hat:.6f} {err:.6f}")

if __name__ == "__main__":
    main()
