import math

def has_inverse(a: int, m: int) -> bool:
    if m <= 0: return False
    return math.gcd(a, m) == 1

def main():
    import sys
    input_data = sys.stdin.read().strip().split()
    if not input_data: return
    q = int(input_data[0])
    idx = 1
    results = []
    for _ in range(q):
        a = int(input_data[idx])
        m = int(input_data[idx+1])
        idx += 2
        results.append("true" if has_inverse(a, m) else "false")
    print("\n".join(results))

if __name__ == "__main__":
    main()
