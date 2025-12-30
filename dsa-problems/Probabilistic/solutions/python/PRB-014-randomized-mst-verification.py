import math
import sys

def min_trials(n: int, C: float) -> int:
    # p is probability of detection per trial
    # Use float for division
    p = 1.0 / (n * n)
    
    # Avoid log(0) if C is exactly 1 (though constraints say C < 1)
    if C >= 1.0:
        return float('inf') # Theoretically impossible
        
    num = math.log(1.0 - C)
    den = math.log(1.0 - p)
    
    return math.ceil(num / den)

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    C = float(data[1])
    print(min_trials(n, C))

if __name__ == "__main__":
    main()
