import sys

def bloomier_stats(m: int, r: int):
    mem = m * r
    fpr = 2.0 ** -r
    return mem, fpr

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    m = int(data[0])
    r = int(data[1])
    mem, fpr = bloomier_stats(m, r)
    print(f"{mem} {fpr:.6f}")

if __name__ == "__main__":
    main()
