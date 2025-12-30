import sys

def two_unique_with_triples_mask(a: list[int], M: int) -> list[int]:
    # 1. Find splitting bit index (must be in M and distinguish the two uniques)
    split_bit = -1
    for i in range(31):
        if not ((M >> i) & 1):
            continue

        count = 0
        for x in a:
            if (x >> i) & 1:
                count += 1

        if count % 3 == 1:
            split_bit = i
            break

    # If no split bit found in M, find any distinguishing bit
    if split_bit == -1:
        for i in range(31):
            count = 0
            for x in a:
                if (x >> i) & 1:
                    count += 1
            if count % 3 == 1:
                split_bit = i
                break

    # 2. Reconstruct (now split_bit is guaranteed to be valid)
    num1, num2 = 0, 0
    for i in range(31):
        c1, c2 = 0, 0
        for x in a:
            bit_val = (x >> i) & 1
            if (x >> split_bit) & 1:
                c2 += bit_val
            else:
                c1 += bit_val

        if c1 % 3 == 1: num1 |= (1 << i)
        if c2 % 3 == 1: num2 |= (1 << i)

    return sorted([num1, num2])

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return

    ptr = 0
    n = int(data[ptr]); ptr += 1
    a = []
    for _ in range(n):
        a.append(int(data[ptr])); ptr += 1
    M = int(data[ptr]); ptr += 1

    result = two_unique_with_triples_mask(a, M)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
