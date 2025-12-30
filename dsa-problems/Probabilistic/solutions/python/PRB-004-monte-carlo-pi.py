import sys
import math
import random

def monte_carlo_pi(N: int, seed: int):
    random.seed(seed)

    count_inside = 0

    for _ in range(N):
        # Generate two random numbers in [0, 1)
        x = random.random()
        y = random.random()

        # Check if point is inside quarter circle
        if x * x + y * y <= 1.0:
            count_inside += 1

    # Calculate pi estimate
    p_hat = count_inside / N
    pi_hat = 4.0 * p_hat

    # Calculate 95% confidence interval half-width
    std_err_p = math.sqrt(p_hat * (1.0 - p_hat) / N)
    error = 1.96 * std_err_p * 4.0

    return pi_hat, error

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    N = int(data[0])
    seed = int(data[1])
    pi_hat, err = monte_carlo_pi(N, seed)
    print(f"{pi_hat:.6f} {err:.6f}")

if __name__ == "__main__":
    main()
