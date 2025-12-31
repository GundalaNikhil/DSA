import math
import sys

def overflow_probability(m: int, k: int, c: int, n: int) -> float:
    lambda_val = (k * n) / m
    max_val = (1 << c) - 1
    
    term = math.exp(-lambda_val)
    total_prob = term
    
    for i in range(1, max_val + 1):
        term *= (lambda_val / i)
        total_prob += term
        
    return 1.0 - total_prob

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    m = int(data[0])
    k = int(data[1])
    c = int(data[2])
    n = int(data[3])
    print(f"{overflow_probability(m, k, c, n):.15f}")

if __name__ == "__main__":
    main()
