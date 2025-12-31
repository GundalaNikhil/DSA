def count_visible(h: list[int]) -> int:
    count = 0
    max_h = -1
    
    for height in h:
        if height > max_h:
            count += 1
            max_h = height
            
    return count


def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if not lines:
        return

    n = int(lines[0])
    h = list(map(int, lines[1].split()))
    result = count_visible(h)
    print(result)

if __name__ == "__main__":
    main()
