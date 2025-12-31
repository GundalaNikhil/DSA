import sys
import math

def poisson_approx(n: int, p: float, k: int):
    lam = n * p

    # Compute exact binomial probability: C(n,k) * p^k * (1-p)^(n-k)
    # Use log space for stability
    if k > n:
        binomial_prob = 0.0
    else:
        try:
            log_binom = math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
            log_binom += k * math.log(p) if p > 0 else (0 if k == 0 else float('-inf'))
            log_binom += (n - k) * math.log(1 - p) if p < 1 else (0 if k == n else float('-inf'))
            binomial_prob = math.exp(log_binom) if log_binom != float('-inf') else 0.0
        except (ValueError, OverflowError):
            binomial_prob = 0.0

    # Compute Poisson approximation: e^{-lambda} * lambda^k / k!
    if lam == 0:
        p_approx = 1.0 if k == 0 else 0.0
    else:
        try:
            log_p = -lam + k * math.log(lam) - math.lgamma(k + 1)
            p_approx = math.exp(log_p)
        except ValueError:
            p_approx = 0.0

    error = abs(binomial_prob - p_approx)

    return binomial_prob, p_approx, error

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    p = float(data[1])
    k = int(data[2])
    binomial, approx, error = poisson_approx(n, p, k)
    print(f"{approx:.9f} {binomial:.9f} {error:.9f}")

if __name__ == "__main__":
    main()
