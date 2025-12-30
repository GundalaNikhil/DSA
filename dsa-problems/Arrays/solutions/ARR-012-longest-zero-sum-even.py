import sys

def longest_zero_sum_even_length(arr: list[int]) -> int:
    # Map stores {sum: {0: first_even_idx, 1: first_odd_idx}}
    # Initialize with None
    idx_map = {}

    # Base case: Sum 0 at index -1 (Odd)
    if 0 not in idx_map:
        idx_map[0] = {0: None, 1: -1}

    current_sum = 0
    max_len = 0

    for i, val in enumerate(arr):
        current_sum += val
        parity = i % 2

        if current_sum not in idx_map:
            idx_map[current_sum] = {0: None, 1: None}

        first_indices = idx_map[current_sum]

        if first_indices[parity] is not None:
            length = i - first_indices[parity]
            if length > max_len:
                max_len = length
        else:
            first_indices[parity] = i

    return max_len

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    result = longest_zero_sum_even_length(arr)
    print(result)

if __name__ == "__main__":
    main()

