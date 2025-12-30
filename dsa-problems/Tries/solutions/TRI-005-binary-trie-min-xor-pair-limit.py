def min_xor_naive(arr, L):
    min_xor = float('inf')
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
            xor_val = arr[i] ^ arr[j]
            if xor_val <= L:
                min_xor = min(min_xor, xor_val)

    return min_xor if min_xor != float('inf') else -1


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
