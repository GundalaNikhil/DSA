import sys

def treap_expectations(n: int):
    H = 0.0
    for i in range(1, n + 1):
        H += 1.0 / i
        
    e_depth = 2 * H - 2
    e_path = 2 * (n + 1) * H - 4 * n
    
    return e_depth, e_path

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    d, p = treap_expectations(n)
    print(f"{d:.6f} {p:.6f}")

if __name__ == "__main__":
    main()
