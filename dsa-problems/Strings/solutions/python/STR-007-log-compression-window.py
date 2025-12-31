def compress_with_window(s: str, w: int) -> str:
    if not s:
        return ""

    result = []
    i = 0
    n = len(s)

    while i < n:
        start = i
        char = s[i]

        # Count consecutive occurrences
        while i < n and s[i] == char:
            i += 1

        run_length = i - start

        # Compress if >= threshold
        if run_length >= w:
            result.append(char + str(run_length))
        else:
            result.append(char * run_length)

    return ''.join(result)


def main():
    import sys


    # Read input
    input_data = sys.stdin.read().strip()
    if not input_data:
        return
        
    parts = input_data.split()
    if len(parts) >= 2:
        s = parts[0]
        try:
            w = int(parts[1])
            print(compress_with_window(s, w))
        except ValueError:
            pass

if __name__ == "__main__":
    main()
