import sys

def solve(arr):
    """
    Battery Lab - First Negative
    Computes some metric based on the array and first negative element
    """
    if not arr:
        return "0"

    # Find first negative
    first_neg_idx = -1
    first_neg_val = None
    for i, val in enumerate(arr):
        if val < 0:
            first_neg_idx = i
            first_neg_val = val
            break

    if first_neg_idx == -1:
        # No negative found - return sum modulo 100
        return str(sum(arr) % 100)

    # With first negative found
    # Compute: sum of elements up to first negative + first negative value
    prefix_sum = sum(arr[:first_neg_idx])
    result = prefix_sum + first_neg_val

    return str(result)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    arr = [int(input_data[i+1]) for i in range(n)]

    result = solve(arr)
    print(result)

if __name__ == "__main__":
    main()
