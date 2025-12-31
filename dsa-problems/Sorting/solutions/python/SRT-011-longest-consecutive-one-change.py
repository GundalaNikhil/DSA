def longest_after_change(arr: list[int]) -> int:
    """Find longest sequence of consecutive integers (by value)"""
    if not arr:
        return 0

    # Use a set to track unique values and build ranges
    num_set = set(arr)
    max_length = 0

    for num in num_set:
        # If this is the start of a sequence, count from here
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = longest_after_change(arr)
    print(result)

if __name__ == "__main__":
    main()
