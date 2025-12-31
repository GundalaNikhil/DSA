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
    input_data = sys.stdin.read().strip().split('\n')

    n, L = map(int, input_data[0].split())
    arr = list(map(int, input_data[1].split()))
    result = min_xor_naive(arr, L)
    print(result)

if __name__ == "__main__":
    main()
