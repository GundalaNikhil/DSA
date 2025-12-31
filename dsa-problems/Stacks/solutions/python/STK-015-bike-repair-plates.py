def count_unsafe(d: list[int]) -> int:
    """
    Count plates marked unsafe during removal.
    A plate is unsafe if it's larger than the plate removed just above it.
    Scanning from top to bottom: as we remove d[i], we check if d[i+1] > d[i].
    """
    unsafe_count = 0
    for i in range(len(d) - 1):
        # When d[i] is removed, d[i+1] is revealed
        # It's unsafe if d[i+1] > d[i]
        if d[i+1] > d[i]:
            unsafe_count += 1
    return unsafe_count


def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    n = int(lines[0])
    d = list(map(int, lines[1].split()))
    result = count_unsafe(d)
    print(result)

if __name__ == "__main__":
    main()
