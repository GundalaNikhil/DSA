import sys

def reservoir_sample(n: int, k: int, seed: int):
    if k == 0:
        return []
    if k > n:
        k = n

    reservoir = list(range(1, k + 1))
    state = seed
    mask = (1 << 64) - 1  # 2^64 - 1

    for i in range(k + 1, n + 1):
        # Generate next random number using specified LCG
        state = (state * 6364136223846793005 + 1) & mask
        j = state % i

        if j < k:
            reservoir[j] = i

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
    print(" ".join(str(x) for x in res))

if __name__ == "__main__":
    main()
