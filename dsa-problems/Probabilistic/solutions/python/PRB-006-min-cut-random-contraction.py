import sys
import math

def min_trials(n: int, P: float) -> int:
    if n < 2:
        return 0
        
    p_success = 2.0 / (n * (n - 1))
    
    # Avoid log(0) if P=1 (though constraints say P < 1)
    if P >= 1.0:
        return float('inf') # Or handle appropriately
        
    numerator = math.log(1.0 - P)
    denominator = math.log(1.0 - p_success)
    
    return math.ceil(numerator / denominator)

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    P = float(data[1])
    print(min_trials(n, P))

if __name__ == "__main__":
    main()
