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
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
