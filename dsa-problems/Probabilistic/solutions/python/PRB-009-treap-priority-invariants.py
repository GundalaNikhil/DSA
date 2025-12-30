import sys

def treap_expectations(n: int):
    H = 0.0
    for i in range(1, n + 1):
        H += 1.0 / i

    return H

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    h = treap_expectations(n)
    print(f"{h:.6f}")

if __name__ == "__main__":
    main()
