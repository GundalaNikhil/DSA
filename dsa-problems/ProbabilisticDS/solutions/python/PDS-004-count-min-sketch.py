import math
import sys

def cms_params(epsilon: float, delta: float):
    w = math.ceil(math.e / epsilon)
    d = math.ceil(math.log(1.0 / delta))
    return w, d

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    epsilon = float(data[0])
    delta = float(data[1])
    w, d = cms_params(epsilon, delta)
    print(f"{w} {d}")

if __name__ == "__main__":
    main()
