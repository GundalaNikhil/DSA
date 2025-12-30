def gray_code(n: int) -> list[str]:
    if n == 1:
        return ["0", "1"]
    
    prev = gray_code(n - 1)
    result = []
    
    # Prefix 0
    for s in prev:
        result.append("0" + s)
        
    # Prefix 1 to reversed
    for s in reversed(prev):
        result.append("1" + s)
        
    return result


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
