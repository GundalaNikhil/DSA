import sys
import random

def reservoir_sample(n: int, k: int, seed: int):
    if k == 0:
        return []
    if k > n:
        k = n

    random.seed(seed)
    reservoir = list(range(1, k + 1))

    for i in range(k, n):
        j = random.randint(0, i)
        if j < k:
            reservoir[j] = i + 1

    return reservoir

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])
    seed = int(data[2])
    res = reservoir_sample(n, k, seed)
    res.sort()
    print(" ".join(str(x) for x in res))

if __name__ == "__main__":
    main()
