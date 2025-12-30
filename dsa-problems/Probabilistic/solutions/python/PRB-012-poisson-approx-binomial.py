import sys
import math

def poisson_approx(n: int, p: float, k: int):
    lam = n * p
    
    # Use log-gamma for factorial: ln(k!) = lgamma(k+1)
    # ln(P) = -lam + k * ln(lam) - lgamma(k+1)
    
    if lam == 0:
        p_approx = 1.0 if k == 0 else 0.0
    else:
        try:
            log_p = -lam + k * math.log(lam) - math.lgamma(k + 1)
            p_approx = math.exp(log_p)
        except ValueError:
            p_approx = 0.0
            
    err = min(1.0, 2.0 * n * p * p)
    
    return p_approx, err

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    p = float(data[1])
    k = int(data[2])
    approx, err = poisson_approx(n, p, k)
    print(f"{approx:.6f} {err:.6f}")

if __name__ == "__main__":
    main()
