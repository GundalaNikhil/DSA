def count_unsafe(d: list[int]) -> int:
    unsafe_count = 0
    for i in range(len(d) - 1):
        if d[i] < d[i+1]:
            unsafe_count += 1
    return unsafe_count


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
