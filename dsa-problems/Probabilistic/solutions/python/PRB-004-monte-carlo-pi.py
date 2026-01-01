import sys
import math


class LCG:
    def __init__(self, seed):
        self.state = seed & 0xFFFFFFFF

    def next_float(self):
        self.state = (self.state * 1664525 + 1013904223) & 0xFFFFFFFF
        return self.state / 4294967296.0

def monte_carlo_pi(N: int, seed: int):
    rng = LCG(seed)

    count_inside = 0

    for _ in range(N):
        # Generate two random numbers in [0, 1)
        x = rng.next_float()
        y = rng.next_float()

        # Check if point is inside quarter circle
        if x * x + y * y <= 1.0:
            count_inside += 1

    # Calculate pi estimate
    p_hat = count_inside / N
    pi_hat = 4.0 * p_hat

    # Calculate 95% confidence interval half-width
    # Avoid division by zero if p_hat is 0 or 1 (edge case)
    if N > 0:
        std_err_p = math.sqrt(p_hat * (1.0 - p_hat) / N)
        error = 1.96 * std_err_p * 4.0
    else:
        error = 0.0

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
